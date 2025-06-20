import os
import logging
from aiogram import Bot, Dispatcher, types, executor

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@buyersclubusa"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    logger.info(f"[START] User @{message.from_user.username} started the bot.")
    await message.answer("✨ Buyer's Club USA Bot activated!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_all_messages(message: types.Message):
    logger.info(f"[MESSAGE] From @{message.from_user.username}: {message.text}")
    await message.answer("I received your message!")

if __name__ == "__main__":
    logger.info("[BOOT] Bot is launching...")
    executor.start_polling(dp, skip_updates=True)
