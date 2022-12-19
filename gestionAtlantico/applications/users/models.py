from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Titulacion(models.Model):
    titulo = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=350, blank=True)
    duracion = models.PositiveIntegerField(blank=True)
    
    class Meta:
        verbose_name = 'Titulación'
        verbose_name_plural = 'Titulaciones'


class User(AbstractUser):
    
    TYPE_CHOICE = (
        ('A', 'ALUMNO'),
        ('P', 'PROFESOR'),
    )
    
    first_name = models.CharField(
        'Nombre', 
        max_length=50
        )
    
    last_name = models.CharField(
        'Apellido', 
        max_length=50
        )
    
    tipo = models.CharField(
        'Alumno o profesor',
        choices=TYPE_CHOICE, 
        max_length=1,
        )
    
    nif = models.CharField(
        'NIF',
        unique=True, 
        max_length=9, 
        )
    
    email_institucional = models.EmailField(
        max_length=150, 
        unique=True
        )
    
    email_personal = models.EmailField(
        max_length=150, 
        unique=True
        )
    
    telefono = models.CharField(
        max_length=9,
        unique=True
        )
    
    titulacion = models.ForeignKey(
        Titulacion, 
        on_delete=models.CASCADE)
    
    curso = models.PositiveIntegerField()
    
    reservas = models.ManyToManyField(
        'reservas.Reservas', 
        related_name="reservas_de_usuario")
    
    USERNAME_FIELD = 'email_institucional'
    REQUIRED_FIELDS = ['username',]
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'