import telebot
import requests
from config import TELEGRAM_BOT_TOKEN, SERVER_URL

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username  # telegram @username

    bot.reply_to(message, "AF Imperiya botiga muvaffaqiyatli ulandingiz!")

    # BACKENDGA yuboramiz
    try:
        requests.post(f"{SERVER_URL}/api/save_chat_id", json={
            "username": username,
            "chat_id": chat_id
        })
    except Exception as e:
        print("Chat ID yuborishda xato:", e)
