# Generated by Django 2.2.10 on 2020-03-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_tiempo_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_tarea',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
