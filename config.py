# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", 60))  # в минутах, по умолчанию 60