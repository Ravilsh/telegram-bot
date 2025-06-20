import os
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = "8135595978:AAF5clMt2GpsfmtRBHyoHqKCnd_CoLEMtuo"
CHANNEL_ID = "@buyersclubusa"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("✨ Buyer's Club USA Bot activated!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# trigger rebuild
