from __future__ import absolute_import, unicode_literals
import pymysql
pymysql.install_as_MySQLdb()
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from test_celery.celery import app as celery_app
