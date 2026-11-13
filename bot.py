import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://t.me/+fBcQi9QfEJBjNTY1"

WELCOME_MESSAGE = """
🎉 <b>WELCOME TO OUR EARNING FAMILY!</b> ❤️

💸 <b>Easily Earn ₹5,000 – ₹10,000</b> 👀😱

✔️ Daily Shopping Offers 🛍️
✔️ Free Cashback Loots 💰
✔️ New Earning Tips & Tricks 🚀

📢 <b>Note:</b> Join our official channel and explore ways to earn money without investment! ❤️😊

👇 Click below to join our channel.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 JOIN CHANNEL", url=CHANNEL_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured.")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
