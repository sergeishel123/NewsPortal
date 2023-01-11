import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('MyProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_email_every_8_hours_on_monday':
        {'task': 'NewsPortal.tasks.send_email_every_8_hours_on_monday',
         'schedule': crontab(
             hour = 8, minute = 0, day_of_week = 'monday'
         ),
         'args': ()
         },
}



