from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField()
    city=models.CharField(max_length=20)
