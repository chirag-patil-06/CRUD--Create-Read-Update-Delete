from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    joining=models.CharField(max_length=30)
    job=models.CharField(max_length=20)