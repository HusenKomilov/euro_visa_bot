from aiogram import types
from tg_bot.bot.utils import dp, bot


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message)
    await message.reply("Assalomu alaykum! Botimizga xush kelibsiz!")



