import logging import os from telegram import Update from telegram.ext import ( Application, CommandHandler, ContextTypes ) from dotenv import load_dotenv from scheduler import start_scheduler from coupon_fetcher import fetch_coupon

── Загрузка переменных окружения ───────────────────────────────────────────

load_dotenv() BOT_TOKEN = os.getenv("BOT_TOKEN")

── Логирование ─────────────────────────────────────────────────────────────

logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO, handlers=[ logging.FileHandler("bot.log", encoding="utf-8"), logging.StreamHandler() ] ) logger = logging.getLogger(name)

── Команда /start ───────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: await update.message.reply_text("🤖 Бот работает. Добро пожаловать!")

── Команда /coupon <store> ──────────────────────────────────────────────────

async def coupon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: if not context.args: await update.message.reply_text("❗ Пожалуйста, укажите магазин. Например: /coupon usa.tommy.com") return

store = context.args[0].lower()
try:
    coupon_text = await fetch_coupon(store)
    if coupon_text:
        await update.message.reply_text(f"🎟 Купон для {store}:

{coupon_text}") else: await update.message.reply_text(f"🚫 Купоны не найдены для {store}.") except Exception as e: logger.error(f"Ошибка при получении купона: {e}") await update.message.reply_text("❌ Произошла ошибка при получении купона. Попробуйте позже.")

── Запуск ────────────────────────────────────────────────────────────────────

if name == "main": logger.info("🚀 Бот запускается...")

application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("coupon", coupon))

start_scheduler()
application.run_polling()
logger.info("✅ Бот запущен")
