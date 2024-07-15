import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='employee_number',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(max_length=12),
        ),
        migrations.AddField(
            model_name='professor',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.category'),
        ),
        migrations.DeleteModel(
            name='Principal',
        ),
    ]
