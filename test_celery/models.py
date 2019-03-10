from django.db import models

class Add(models.Model):
    task_id = models.CharField(max_length=128)
    first = models.IntegerField()
    second = models.IntegerField()
    log_date = models.DateTimeField()
