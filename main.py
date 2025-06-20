import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from datetime import datetime

# Настройка логирования в файл и консоль
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs.txt")
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@buyersclubusa"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user = message.from_user.username or "unknown"
    logger.info(f"[START] User @{user} started the bot.")
    await message.answer("✨ Buyer's Club USA Bot activated!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_all_messages(message: types.Message):
    user = message.from_user.username or "unknown"
    text = message.text
    logger.info(f"[MESSAGE] From @{user}: {text}")
    await message.answer("I received your message!")

if __name__ == "__main__":
    logger.info("[BOOT] Bot is launching...")
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logger.exception(f"[CRITICAL] Bot crashed with error: {e}")
