import telebot
from config import Config

bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)
SERVER_URL = Config.SERVER_URL

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Assalomu alaykum! Bot ishlayapti.")

# Backend bilan bog‘lanish uchun webhook bo‘lsa ham shu yerga yoziladi
