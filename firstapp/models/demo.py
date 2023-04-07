from django.db import models
from django.db.models import Model

class Demo(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
