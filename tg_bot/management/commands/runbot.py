from django.core.management.base import BaseCommand
from tg_bot.bot.utils import dp, bot
from aiogram import executor


class Command(BaseCommand):
    help = 'Run bot in poolling'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bot started"))
        executor.start_polling(dp)
