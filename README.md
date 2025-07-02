# 🤖 Stake Mines Provably Fair Telegram Bot

A smart Telegram bot that predicts safe and mine tiles from Stake.com's Mines game using provably fair seed logic.

## 📦 Features
- Safe/Mine tile prediction using HMAC + SHA256
- Telegram bot commands
- VIP access system
- Admin panel (ban, promote, stats)
- Accuracy logging
- Game board image output

## 🧠 Commands
- `/check serverSeed clientSeed nonce mines`
- `/addvip @username`
- `/removevip @username`
- `/ban @username`
- `/unban @username`
- `/stats`
- `/users`

## 🚀 Deploy on Render.com
1. Fork or upload this repo to your GitHub.
2. Go to [Render](https://render.com), click **New Web Service**.
3. Connect your GitHub & choose this repo.
4. Set build command:
   ```bash
   pip install -r requirements.txt
