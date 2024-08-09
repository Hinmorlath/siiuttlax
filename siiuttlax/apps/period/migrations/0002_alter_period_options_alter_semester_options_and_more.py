from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['id'], 'verbose_name': 'Periodo', 'verbose_name_plural': 'Periodos'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['id'], 'verbose_name': 'Cuatrimestre', 'verbose_name_plural': 'Cuatrimestres'},
        ),
        migrations.AddField(
            model_name='period',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='period',
            name='cicle',
            field=models.CharField(default='2023 - 2024', max_length=10, verbose_name='Ciclo'),
        ),
        migrations.AlterField(
            model_name='period',
            name='period',
            field=models.CharField(choices=[('Ene-Abr', 'enero - abri'), ('May-Ago', 'mayo - agosto'), ('Sep-Dic', 'septiembre - diciembre')], max_length=10, verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='period',
            name='year',
            field=models.IntegerField(default=2024, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(max_length=2, verbose_name='Cuatrimestre'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(max_length=10, verbose_name='Cuatrimestre en letra'),
        ),
        migrations.AlterModelTable(
            name='semester',
            table=None,
        ),
    ]
