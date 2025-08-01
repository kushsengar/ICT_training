from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    
    
