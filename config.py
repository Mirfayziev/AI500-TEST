import os


class Config:
    """Base configuration for AF Imperiya app."""
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///instance/af_imperiya.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Telegram
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    # e.g. https://ai500-test.onrender.com  (no slash at the end)
    SERVER_URL = os.environ.get("SERVER_URL", "")


# Backwards-compatibility for direct imports
TELEGRAM_BOT_TOKEN = Config.TELEGRAM_BOT_TOKEN
SERVER_URL = Config.SERVER_URL

class Config:
    # ... oldingi sozlamalar

    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    SERVER_URL = os.environ.get("SERVER_URL", "")  # https://web-production-aa3b.up.railway.app
    ENABLE_WEBHOOK = os.environ.get("ENABLE_WEBHOOK", "false").lower() == "true"
