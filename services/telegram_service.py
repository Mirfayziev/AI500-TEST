import telebot
from config import Config

TOKEN = Config.TELEGRAM_BOT_TOKEN
bot = telebot.TeleBot(TOKEN)

def send_push(chat_id, message):
    try:
        bot.send_message(chat_id, message)
        return True
    except Exception as e:
        print("Telegram push error:", e)
        return False
