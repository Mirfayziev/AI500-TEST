import telebot
from config import Config

bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)

def send_push(chat_id, message):
    try:
        bot.send_message(chat_id, message)
        return True
    except Exception as e:
        print("Telegram push error:", e)
        return False
