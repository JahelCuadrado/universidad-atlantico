# Generated by Django 4.1.3 on 2022-12-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_material_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='imagen',
            field=models.ImageField(null=True, upload_to='clases/'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='equipos/'),
        ),
        migrations.AlterField(
            model_name='material',
            name='fecha_modificacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificación del material'),
        ),
        migrations.AlterField(
            model_name='material',
            name='imagen',
            field=models.ImageField(null=True, upload_to='material/'),
        ),
    ]