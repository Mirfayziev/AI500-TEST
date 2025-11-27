import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def send_push(chat_id, text):
    """
    Global push sender.
    Xodim → Rahbar → Xodim reaksiyalarini yuboradi.
    """
    if not chat_id:
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text})
    except Exception as e:
        print("Telegram push error:", e)
