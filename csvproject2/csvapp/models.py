from django.db import models
class Product(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	price=models.IntegerField()
	warenty=models.CharField(max_length=100)
	stock=models.IntegerField()
# Create your models here.
