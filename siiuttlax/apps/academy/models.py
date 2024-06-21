from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(User):
    employee_number = models.IntegerField(verbose_name='Número de Empleado')

class Student(User):
    enrollment = models.CharField(max_length=12, verbose_name='Matrícula')


class Principal(User):
    nickname = models.CharField(max_length=50, verbose_name='Apodo')

   
