from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def game_menu():
    keyboard = [
        [InlineKeyboardButton("🚀 Lucky Jet", callback_data="lucky_jet"),
         InlineKeyboardButton("💣 Mines", callback_data="mines")],
        [InlineKeyboardButton("👑 Royal Mines", callback_data="royal_mines"),
         InlineKeyboardButton("🛩️ Aviator", callback_data="aviator")],
        [InlineKeyboardButton("🌕 CoinFlip", callback_data="coinflip"),
         InlineKeyboardButton("💀 Brawl Pirates", callback_data="pirates")],
        [InlineKeyboardButton("⭐ Mines Mi", callback_data="mines_mi"),
         InlineKeyboardButton("💣 Bombucks", callback_data="bombucks")],
        [InlineKeyboardButton("⚽ Penalty Shoot", callback_data="penalty"),
         InlineKeyboardButton("⚽ Football X", callback_data="football")],
        [InlineKeyboardButton("💣 1win Mines", callback_data="1win")],
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)
