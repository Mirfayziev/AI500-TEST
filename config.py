import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///instance/af_imperiya.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Telegram bot
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

    # Render domain (webhook uchun)
    SERVER_URL = os.environ.get("SERVER_URL")
