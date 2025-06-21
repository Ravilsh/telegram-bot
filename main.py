import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from scheduler import start_scheduler

# Загрузка переменных
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# /start
async def start(update, context):
    await update.message.reply_text("🤖 Бот работает. Добро пожаловать!")

# Любые текстовые сообщения
async def handle_message(update, context):
    await update.message.reply_text("Hello, R S! 👋\nI received your message!")

# Приложение
application = Application.builder().token(BOT_TOKEN).build()

# Хендлеры
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Планировщик
start_scheduler()

# Запуск
if __name__ == "__main__":
    logging.info("🚀 Бот запущен")
    application.run_polling()
