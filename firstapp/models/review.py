from django.db import models
from django.db.models import Model


class Review(models.Model):
    rating = models.IntegerField(default=0,primary_key=True)
    productname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)



"""    @staticmethod
    def get_productpics_by_id(ids):
        return Recomendation.objects.filter(id__in=ids)"""
