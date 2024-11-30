from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Вказуємо, що налаштування Django доступні для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Використовуємо налаштування Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматичне виявлення завдань
app.autodiscover_tasks()