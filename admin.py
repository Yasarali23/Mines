from telegram import Update
from telegram.ext import ContextTypes
from database import add_vip, remove_vip, ban_user, unban_user, load_json
from config import ADMINS

async def handle_admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMINS:
        await update.message.reply_text("⛔ Admins only.")
        return

    command = update.message.text.split()[0][1:]
    args = context.args
    if len(args) == 0:
        await update.message.reply_text("❌ Please provide a user ID or @username.")
        return

    target = args[0].replace("@", "")

    if command == "addvip":
        add_vip(target)
        await update.message.reply_text(f"✅ {target} added to VIP list.")
    elif command == "removevip":
        remove_vip(target)
        await update.message.reply_text(f"❌ {target} removed from VIP list.")
    elif command == "ban":
        ban_user(target)
        await update.message.reply_text(f"🚫 {target} has been banned.")
    elif command == "unban":
        unban_user(target)
        await update.message.reply_text(f"♻️ {target} unbanned.")
    elif command == "stats":
        logs = load_json("accuracy.json")
        response = "\n".join(
            [f"@{k}: {len(v)} checks, avg {sum(i['accuracy'] for i in v)/len(v):.2f}%" for k, v in logs.items()]
        )
        await update.message.reply_text(response or "No logs.")
    elif command == "users":
        users = load_json("users.json")
        msg = f"VIPs: {users.get('vip', [])}\nBanned: {users.get('banned', [])}"
        await update.message.reply_text(msg)
