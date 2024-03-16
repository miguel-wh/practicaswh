# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

CELERY_TIMEZONE = 'America/Mexico_City'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TASK_RESULT_EXPIRES = 604800  # 7 Dias

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mascotas_project.settings')

app = Celery('mascotas_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')