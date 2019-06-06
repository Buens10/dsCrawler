import os
from celery import Celery


os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'dsCrawler.settings')

app = Celery('dsCrawler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))