from django.db import models
from django.db.models import Model

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
