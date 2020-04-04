# Generated by Django 2.2.10 on 2020-04-01 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20200401_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='id',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='recurso',
            old_name='id',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='id',
            new_name='codigo',
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='usuario_cambio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso', to_field='id'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creacion_proyecto', to='gestion.Recurso', to_field='id'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Proyecto', to_field='id'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creacion_tarea', to='gestion.Recurso', to_field='id'),
        ),
        migrations.AlterField(
            model_name='tiempo_tarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Tarea', to_field='id'),
        ),
        migrations.AlterField(
            model_name='tiempo_tarea',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso', to_field='id'),
        ),
        migrations.AlterField(
            model_name='validacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso', to_field='id'),
        ),
    ]