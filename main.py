import logging
import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from scheduler import start_scheduler

# ── Load .env ───────────────────────
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ── Logging ─────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# ── /start command ─────────────────
async def start(update, context):
    await update.message.reply_text("🤖 Бот работает. Добро пожаловать!")

# ── Init & Start bot properly ──────
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Планировщик запускается сразу
start_scheduler()

# Запуск в фоновом режиме без run_polling()
async def run():
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    # updater.idle() не нужен на Railway

import asyncio
asyncio.get_event_loop().create_task(run())
