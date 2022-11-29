from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
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
        blank=True
        )
    nif = models.CharField(
        'NIF',
        unique=True, 
        max_length=9, 
        blank=True
        )
    titulacion = models.CharField(
        max_length=50, 
        blank=True
        )
    curso = models.CharField(
        max_length=50, 
        blank=True
        )
    email_institucional = models.EmailField(
        max_length=150, 
        blank=True
        )
    email_personal = models.EmailField(
        max_length=150, 
        blank=True
        )
    telefono = models.CharField(
        max_length=9,
        blank=True
        )
    #TODO campo de reservas
    #TODO curso y titulación se escribe o se coge de otra tabla