# trendsSync/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trendsSync.settings')

app = Celery('trendsSync')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'print-time-every-1-minutes': {
        'task': 'myapp.tasks.print_current_time',
        'schedule': 60,  # 1 minutes in seconds
    },
}

app.conf.imports = ('myapp.tasks',)
