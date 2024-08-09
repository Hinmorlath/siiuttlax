import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('period', '0002_alter_period_options_alter_semester_options_and_more'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('TSU', 'Técnico Superior Universitario'), ('Ing', 'Ingeniería'), ('Lic', 'Licenciatura'), ('M', 'Maestría')], max_length=10, verbose_name='Nivel')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, verbose_name='Abreviatura')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'carrera',
                'verbose_name_plural': 'carreras',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('total_hours', models.IntegerField(default=0, verbose_name='Horas totales')),
                ('semanal_hours', models.IntegerField(default=0, verbose_name='Horas semanales')),
                ('file', models.FileField(blank=True, null=True, upload_to='asignaturas/', verbose_name='Archivo')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careers.career', verbose_name='Carrera')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.semester', verbose_name='Cuatrimestre')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
                'ordering': ['career', 'semester'],
            },
        ),
    ]
