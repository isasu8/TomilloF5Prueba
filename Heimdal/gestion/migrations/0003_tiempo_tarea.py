# Generated by Django 2.2.10 on 2020-03-31 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200330_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiempo_Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('horas', models.IntegerField()),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso')),
            ],
        ),
    ]
