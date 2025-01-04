from django.db import models

# Create your models here.
class Product(models.Model):
    prodid=models.CharField(max_length=20, primary_key=True)
    prodname=models.CharField(max_length=30)
    qty=models.IntegerField()
    price=models.FloatField()
    