# Generated by Django 4.1.3 on 2022-12-13 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(max_length=350, verbose_name='Descripción de la clase'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_alta',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de alta de la clase'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_modificacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de alta de la clase'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre de la clase'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='descripcion',
            field=models.CharField(max_length=350, verbose_name='Descripción del material'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del material'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='numero_equipo',
            field=models.CharField(max_length=150, unique=True, verbose_name='Numero de equipo'),
        ),
        migrations.AlterField(
            model_name='material',
            name='descripcion',
            field=models.CharField(max_length=350, verbose_name='Descripción del material'),
        ),
        migrations.AlterField(
            model_name='material',
            name='inventario',
            field=models.CharField(max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='Numero de inventario'),
        ),
        migrations.AlterField(
            model_name='material',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del material'),
        ),
        migrations.AlterField(
            model_name='material',
            name='serial',
            field=models.CharField(max_length=150, unique=True, verbose_name='Numero de serie'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='clase',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.clase'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='devuelto',
            field=models.BooleanField(verbose_name='Ha sido devuelto'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='equipo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.equipo'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_devolucion',
            field=models.DateField(verbose_name='Fecha de devolución'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='material',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.material'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='motivo_prestamo',
            field=models.CharField(max_length=250, verbose_name='Motivo del préstamo'),
        ),
    ]