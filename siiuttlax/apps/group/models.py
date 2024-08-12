from django.db import models

from apps.period.models import Semester, Period
from apps.academy.models import  Professor, Student
from apps.careers.models import Career

# Create your models here.
class Group(models.Model):
    group = models.CharField(max_length=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    carrer = models.ForeignKey(Career, on_delete=models.CASCADE)
    
def __str__(self):
    return f"{self.semester} - {self.group} - {self.carrer}"