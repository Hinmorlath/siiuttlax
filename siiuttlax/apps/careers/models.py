from django.db import models
from apps.period.models import Semester
from apps.academy.models import Professor



class careers(models.Model):
    LEVEL_CHOICES = [
        ('TSU', 'Tecnico Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria')
    ]

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    year_plan = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(careers, on_delete=models.CASCADE)
    semester = models.IntegerField()
    total_horas = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)

def __str__(self):
        return f"{self.LEVEL_CHOICES} - {self.name}" 




class Professor(models.Model):
     professor = models.ForeignKey(
           name= models.CharField(max_length=100)
           subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
           )
          
     
def __str__(self):
        return f"{self.LEVEL_CHOICES} - {self.name}" 



class  Semester(models.Model):
     semester = models.ForeignKey(
           number = models.IntegerField()
     )
def __str__(self):
        return f"{self.LEVEL_CHOICES} - {self.name}" 