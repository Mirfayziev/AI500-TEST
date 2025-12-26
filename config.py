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

    # AI / LLM (OpenAI-compatible)
    # Examples:
    # - OpenAI:        AI_API_BASE=https://api.openai.com/v1
    # - Other gateway: AI_API_BASE=https://<provider>/v1
    # Required for live mode: AI_API_KEY
    AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.openai.com/v1").rstrip("/")
    AI_API_KEY = os.environ.get("AI_API_KEY", "")
    AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o-mini")
    AI_TIMEOUT_SECONDS = int(os.environ.get("AI_TIMEOUT_SECONDS", "60"))
    AI_MAX_TOKENS = int(os.environ.get("AI_MAX_TOKENS", "600"))
    AI_TEMPERATURE = float(os.environ.get("AI_TEMPERATURE", "0.4"))


# Backwards-compatibility for direct imports
TELEGRAM_BOT_TOKEN = Config.TELEGRAM_BOT_TOKEN
SERVER_URL = Config.SERVER_URL
