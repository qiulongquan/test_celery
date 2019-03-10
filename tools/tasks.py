from __future__ import absolute_import
from celery import shared_task
import time

@shared_task(track_started=True)
# 你很可能在可重用的 Django APP 中编写了一些任务，
# 但是 Django APP 不能依赖于具体的 Django 项目，
# 所以你无法直接导入 Celery 实例。
# @shared_task 装饰器能让你在没有具体的 Celery 实例时创建任务：
def add(x, y):
    time.sleep(30)
    return x + y

