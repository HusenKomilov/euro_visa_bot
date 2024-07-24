from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'tg_bot.tasks.send_daily_message',
        'schedule': crontab(minute='*/1'),
    },
}

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
app.conf.timezone = 'Asia/Tashkent'
