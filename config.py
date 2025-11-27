import os

# === FLASK SECRET ===
SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

# === TELEGRAM BOT TOKEN ===
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# === SERVER URL (Render domain) ===
SERVER_URL = os.environ.get("SERVER_URL")

# === DATABASE ===
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "sqlite:///instance/af_imperiya.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
