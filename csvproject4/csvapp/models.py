from django.db import models
class Bank(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	amount=models.IntegerField()
	city=models.CharField(max_length=100)
# Create your models here.
