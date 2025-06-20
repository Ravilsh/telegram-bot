import os
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@buyersclubusa"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(f"[START] User @{message.from_user.username} started the bot.")
    await message.answer("✨ Buyer's Club USA Bot activated!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_all_messages(message: types.Message):
    print(f"[MESSAGE] From @{message.from_user.username}: {message.text}")
    await message.answer("I received your message!")

if name == "main":
    print("[BOOT] Bot is launching...")
    executor.start_polling(dp, skip_updates=True)
