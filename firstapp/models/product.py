from django.db import models
from django.db.models import Model
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desc = models.CharField(max_length=250,default='', null = True, blank = True )
    image = models.ImageField(upload_to='uploads/products')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
