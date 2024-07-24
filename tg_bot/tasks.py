from celery import shared_task
from aiogram import Bot
from dotenv import load_dotenv
import os
from config.celery import app as celery_app

load_dotenv()
from tg_bot.bot.utils import bot
import requests

TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = 2131715946
import asyncio
from tg_bot.utils import main


@celery_app.task
def send_daily_message():
    print("START TASK")
    data = main().keys()
    if len(data) != 0:
        text = "Registratsiya ochilgan"
    else:
        text = "Registratsiya ochilmagan"
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
    requests.post(url, params=params)

