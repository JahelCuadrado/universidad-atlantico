# Generated by Django 4.1.3 on 2022-12-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0008_clase_imagen_equipo_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservas',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='material',
        ),
        migrations.AddField(
            model_name='reservas',
            name='clase',
            field=models.ManyToManyField(blank=True, to='reservas.clase'),
        ),
        migrations.AddField(
            model_name='reservas',
            name='equipo',
            field=models.ManyToManyField(blank=True, to='reservas.equipo'),
        ),
        migrations.AddField(
            model_name='reservas',
            name='material',
            field=models.ManyToManyField(blank=True, to='reservas.material'),
        ),
    ]