import os
from aiogram import Dispatcher, Bot

TOKEN = os.getenv("TG_TOKEN")

bot = Bot(token="6281073009:AAHk0eRh05IVbl1th_1MA22Y9rTqG_v7ARA")
dp = Dispatcher(bot)


async def start_bot():
    await dp.start_polling()
