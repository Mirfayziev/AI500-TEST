import os


class Config:
    """Railway-ready configuration for AF Imperiya app."""

    # =========================
    # Flask
    # =========================
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

    # =========================
    # Database (Railway-safe)
    # =========================
    _raw_db_url = os.getenv("DATABASE_URL", "").strip()

    if _raw_db_url:
        # Railway Postgres ba’zan postgres:// beradi
        SQLALCHEMY_DATABASE_URI = _raw_db_url.replace(
            "postgres://", "postgresql://", 1
        )
    else:
        # Lokal yoki fallback
        SQLALCHEMY_DATABASE_URI = "sqlite:///instance/af_imperiya.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =========================
    # Telegram
    # =========================
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

    # Masalan: https://web-production-aa3b.up.railway.app
    SERVER_URL = os.getenv("SERVER_URL", "").rstrip("/")

    # Webhook faqat flag true bo‘lsa ishlaydi
    ENABLE_WEBHOOK = os.getenv("ENABLE_WEBHOOK", "false").lower() == "true"


# ======================================
# Backwards compatibility (agar eski importlar bo‘lsa)
# ======================================
TELEGRAM_BOT_TOKEN = Config.TELEGRAM_BOT_TOKEN
SERVER_URL = Config.SERVER_URL
ENABLE_WEBHOOK = Config.ENABLE_WEBHOOK
