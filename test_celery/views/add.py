#__*__coding:utf-8__*__

from celery.result import AsyncResult
from django.shortcuts import render_to_response

from tools.tasks import add
from test_celery.models import Add
from tools.db import Db
import datetime


def index(request):
    return  render_to_response('index.html')

def add_1(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    result = add.delay(first,second)
    dd = Add(task_id=result.id,first=first,second=second,log_date=datetime.datetime.now())
    dd.save()
    return render_to_response('index.html')

# 任务结果
def results(request):
    #查询所有的任务信息
    db = Db()
    rows = db.get_tasksinfo()
    return render_to_response('result.html',{'rows':rows})