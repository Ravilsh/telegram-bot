# main.py

import logging
import os
import asyncio
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from scheduler import start_scheduler
from publisher import publish_deals

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Обработчик команды /start
async def start(update, context):
    await update.message.reply_text("🤖 Бот работает. Добро пожаловать!")

# Создание и запуск приложения
application = Application.builder().token(BOT_TOKEN).build()

# Добавление хендлеров
application.add_handler(CommandHandler("start", start))

# Запуск планировщика
start_scheduler()

# Ручной запуск публикации при старте для проверки
async def startup():
    logging.info("🚀 Бот запущен")
    await publish_deals()

if __name__ == "__main__":
    asyncio.run(startup())
    application.run_polling()
