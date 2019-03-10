from __future__ import absolute_import

import os

from celery import Celery
import time
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')

from django.conf import settings  # noqa

app = Celery('test_celery')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)   # 创建了一个 Celery 任务 add，当函数被 @app.task 装饰后，就成为可被 Celery 调度的任务；
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

