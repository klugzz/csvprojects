from django.db import models
class Student(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	age=models.IntegerField()
	city=models.CharField(max_length=100)
# Create your models here.
