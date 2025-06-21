# buyersclub_bot/publisher.py
import os
import logging
from aiogram import Bot

# ── Переменные окружения ────────────────────────────────────────────────────
BOT_TOKEN   = os.getenv("BOT_TOKEN")
CHANNEL_ID  = os.getenv("CHANNEL_ID")       # пример: "@buyersclubusa"

# ── Настройка логирования ───────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ── Инициализируем бота только один раз ─────────────────────────────────────
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")


async def publish_deals() -> None:
    """
    Публикует подборку скидок в Telegram-канал.
    (Пока — статичный текст-заглушка, позже подменим на реальные данные
     из модуля scraper/fetcher.)
    """
    try:
        message = (
            "🔥 <b>New Deals Available!</b> 🔥\n"
            "👟 <b>Nike</b> — Up to 50 % Off\n"
            "🧥 <b>Uniqlo</b> — Extra 20 % Clearance\n"
            "🛍 <b>Macy’s</b> — Buy One Get One Free\n\n"
            "#buyersclub #usa #deals"
        )

        await bot.send_message(chat_id=CHANNEL_ID,
                               text=message,
                               disable_web_page_preview=True)

        logger.info("✅ Deals published successfully")

    except Exception as e:
        logger.error(f"❌ Failed to publish deals: {e}")