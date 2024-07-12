from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=15)
    description = models.TextField()

class Professor(User):
    employee_number = models.CharField(max_length=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)

class Student(User):
    enrollment = models.CharField(max_length=12)