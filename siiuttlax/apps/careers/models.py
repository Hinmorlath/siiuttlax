from django.db import models

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
    year_plan = models.CharField(max_length=10, null=True)
    status = models.BooleanField(default=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(careers, on_delete=models.CASCADE)
    semester = models.IntegerField()
    total_horas = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)
