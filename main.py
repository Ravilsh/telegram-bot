import os
import logging
from aiogram import Bot, Dispatcher, types, executor

# Настройка логирования в консоль и файл
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(),                         # В консоль
        logging.FileHandler("bot.log", encoding="utf-8") # В файл
    ]
)
logger = logging.getLogger(__name__)

# Токен и ID канала
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@buyersclubusa"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    logger.info(f"[START] User @{message.from_user.username} started the bot.")
    await message.answer("✨ Buyer's Club USA Bot activated!")

# Обработка любых текстовых сообщений
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_all_messages(message: types.Message):
    logger.info(f"[MESSAGE] From @{message.from_user.username}: {message.text}")
    await message.answer(f"Hello, {message.from_user.full_name}! 👋\nI received your message!")

# Запуск бота
if __name__ == "__main__":
    logger.info("[BOOT] Bot is launching...")
    executor.start_polling(dp, skip_updates=True)
