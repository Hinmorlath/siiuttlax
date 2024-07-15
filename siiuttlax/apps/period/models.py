from django.db import models

class Period(models.Model):
    PERIODS = [
        ('Ene-Abr', 'enero - abri'),
        ('May-Ago', 'mayo - agosto'),
        ('Sep-Dic', 'septiembre - diciembre')
    ]
    period = models.CharField(max_length=10, choices=PERIODS, verbose_name='Periodo')
    year = models.IntegerField(verbose_name='Año', default=2024)
    cicle = models.CharField(max_length=10, default='2023 - 2024', verbose_name='Ciclo')
    is_active = models.BooleanField(verbose_name='Activo', default=False)
    
    def _str_(self):
        return f'{self.period} {self.year}'
    
    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering = ['id']


class Semester(models.Model):
    semester = models.CharField(max_length=2, verbose_name='Cuatrimestre')
    semester_name = models.CharField(max_length=10, verbose_name="Cuatrimestre en letra")

    def __str__(self):
        return f'{self.semester}'
    

    class Meta:
        verbose_name = 'Cuatrimestre'
        verbose_name_plural = 'Cuatrimestres'
        ordering = ['id']