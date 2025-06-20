import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import os

# Настройка логирования в файл и консоль
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("logs.txt", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Получаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    username = message.from_user.username or "unknown"
    logger.info(f"[START] User: {username} (id={message.from_user.id})")
    await message.answer(f"👋 Hello, {message.from_user.full_name}")
Welcome to Buyer's Club USA Bot!")

# Обработка всех остальных сообщений
@dp.message()
async def echo_handler(message: Message) -> None:
    username = message.from_user.username or "unknown"
    logger.info(f"[MESSAGE] From @{username} (id={message.from_user.id}): {message.text}")
    try:
        await message.reply("🤖 I'm a bot, I received your message!")
    except Exception as e:
        logger.exception(f"[ERROR] Failed to handle message from @{username}: {e}")

# Основная функция запуска бота
async def main():
    logger.info("[BOOT] Bot is launching...")
    try:
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        logger.critical(f"[CRITICAL] Bot crashed with error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
