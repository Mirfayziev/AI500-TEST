import requests
from config import TELEGRAM_BOT_TOKEN

def send_push(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        requests.post(url, json=payload)
    except Exception as e:
        print("Push xatosi:", e)
