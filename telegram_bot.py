import os
import telebot
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SERVER_URL = os.getenv("SERVER_URL")  # Render domening

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username

    bot.reply_to(message, "AF Imperiya tizimiga muvaffaqiyatli bog'landingiz!")

    # serverga chat_id yuborish
    try:
        requests.post(f"{SERVER_URL}/api/save_chat_id", json={
            "username": username,
            "chat_id": chat_id
        })
    except:
        pass

print("Telegram bot ishga tushdi...")
bot.infinity_polling()
