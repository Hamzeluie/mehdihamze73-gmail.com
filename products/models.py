from django.db import models
from datetime import datetime


class ProductGroup(models.Model):
    group_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)


class Product(models.Model):
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=999)
    is_active = models.BooleanField(verbose_name='active', default=True)
