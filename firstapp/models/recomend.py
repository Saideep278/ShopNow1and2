from django.db import models
from django.db.models import Model


class Recomendation(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/recproducts')


    @staticmethod
    def get_productpics_by_id(ids):
        return Recomendation.objects.filter(id__in=ids)
