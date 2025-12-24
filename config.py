import os


class Config:
    """Base configuration for AF Imperiya app."""
    # Flask
    # NOTE: Production'da SECRET_KEY ni env orqali qo'ying (random, uzun).
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Database
    _db_uri = os.environ.get("DATABASE_URL", "sqlite:///instance/af_imperiya.db")
    # Railway/Heroku kabi platformalarda postgres:// bo'lishi mumkin
    if _db_uri.startswith("postgres://"):
        _db_uri = _db_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "uploads")
    MAX_CONTENT_LENGTH = int(os.environ.get("MAX_CONTENT_LENGTH", 25 * 1024 * 1024))  # 25MB
    ALLOWED_EXTENSIONS = set(
        ext.strip().lower()
        for ext in os.environ.get(
            "ALLOWED_EXTENSIONS",
            "png,jpg,jpeg,gif,webp,pdf,doc,docx,xls,xlsx,csv,txt",
        ).split(",")
        if ext.strip()
    )

    # Telegram
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    # e.g. https://your-app.railway.app (no slash at the end)
    # render.yaml'da TELEGRAM_WEBHOOK_URL ham ishlatilgan bo'lishi mumkin
    SERVER_URL = os.environ.get("SERVER_URL") or os.environ.get("TELEGRAM_WEBHOOK_URL", "")
    # Telegram bot polling -> serverga /api/save_chat_id yuboradigan flow uchun (ixtiyoriy)
    TELEGRAM_LINK_TOKEN = os.environ.get("TELEGRAM_LINK_TOKEN", "")


# Backwards-compatibility for direct imports
TELEGRAM_BOT_TOKEN = Config.TELEGRAM_BOT_TOKEN
SERVER_URL = Config.SERVER_URL
