# main.py

import asyncio
import logging
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os
from scheduler import start_scheduler

# Загрузка переменных из .env
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

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Запуск планировщика публикаций
    start_scheduler()

    logging.info("🚀 Бот запущен")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())