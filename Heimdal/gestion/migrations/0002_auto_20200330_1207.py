# Generated by Django 2.2.10 on 2020-03-30 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='asginados_proyecto', to='gestion.Recurso'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='asignados_tarea', to='gestion.Recurso'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creacion_proyecto', to='gestion.Recurso'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creacion_tarea', to='gestion.Recurso'),
        ),
    ]
