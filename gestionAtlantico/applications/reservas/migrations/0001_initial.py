# Generated by Django 4.1.3 on 2022-12-13 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre del material')),
                ('descripcion', models.CharField(blank=True, max_length=350, verbose_name='Descripción del material')),
                ('numero_clase', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='Numero de clase')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta del material')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de alta del material')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre del material')),
                ('descripcion', models.CharField(blank=True, max_length=350, verbose_name='Descripción del material')),
                ('numero_equipo', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Numero de equipo')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta del material')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de alta del material')),
                ('numero_clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.clase')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre del material')),
                ('descripcion', models.CharField(blank=True, max_length=350, verbose_name='Descripción del material')),
                ('serial', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Numero de serie')),
                ('inventario', models.CharField(blank=True, max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='Numero de inventario')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta del material')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de alta del material')),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_prestamo', models.CharField(blank=True, max_length=250, verbose_name='Motivo del préstamo')),
                ('fecha_reserva', models.DateField(auto_now_add=True, verbose_name='Fecha de reserva')),
                ('fecha_devolucion', models.DateField(blank=True, verbose_name='Fecha de devolución')),
                ('devuelto', models.BooleanField(blank=True, verbose_name='Ha sido devuelto')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.clase')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.equipo')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.material')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]