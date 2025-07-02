from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN, ADMINS
from mines_finder import get_mines
from image_creator import generate_board_image
from database import is_vip, is_banned, log_accuracy
from admin import handle_admin_command
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Stake Mines Bot!\nUse /check serverSeed clientSeed nonce mines\nOnly VIP users allowed.\nAdmins: /addvip, /ban, /stats")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or str(user_id)

    if is_banned(user_id):
        await update.message.reply_text("⛔ You are banned.")
        return
    if not is_vip(user_id):
        await update.message.reply_text("🔐 VIP access required. Contact admin.")
        return

    try:
        server_seed = context.args[0]
        client_seed = context.args[1]
        nonce = int(context.args[2])
        mines = int(context.args[3])

        mine_tiles, safe_tiles = get_mines(server_seed, client_seed, nonce, mines)
        img_path = generate_board_image(mine_tiles, safe_tiles, f"board_{user_id}.png")

        correct_safe = len(safe_tiles)
        total_tiles = 25 - mines
        accuracy = round((correct_safe / total_tiles) * 100, 2)
        log_accuracy(user_id, username, accuracy)

        caption = f"✅ Safe Tiles: {sorted(safe_tiles)}\n💣 Mines: {sorted(mine_tiles)}\n🎯 Accuracy: {accuracy}%"
        await update.message.reply_photo(photo=open(img_path, 'rb'), caption=caption)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}\nUsage:\n/check serverSeed clientSeed nonce mines")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_admin_command(update, context)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check", check))
app.add_handler(CommandHandler(["addvip", "removevip", "ban", "unban", "stats", "users"], admin))

app.run_polling()
