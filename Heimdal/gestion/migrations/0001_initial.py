# Generated by Django 2.2.10 on 2020-03-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion_corta', models.CharField(max_length=140)),
                ('descripcion_larga', models.CharField(max_length=255, null=True)),
                ('estado', models.CharField(max_length=1, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_final', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.CharField(max_length=1)),
                ('imagen', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion_corta', models.CharField(max_length=140)),
                ('descripcion_larga', models.CharField(max_length=255, null=True)),
                ('prioridad', models.CharField(max_length=1, null=True)),
                ('estado', models.CharField(max_length=1, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_final', models.DateTimeField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Proyecto')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso'),
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cambio', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('auditoria_id', models.IntegerField()),
                ('usuario_cambio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Recurso')),
            ],
        ),
    ]
