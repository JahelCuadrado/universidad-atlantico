from django.db import models
from applications.users.models import User

# Create your models here.

class Material(models.Model):
    
    nombre = models.CharField(
        "Nombre del material", 
        max_length=50)
    
    imagen = models.ImageField(upload_to='material/', null=True)
    
    descripcion = models.CharField(
        "Descripción del material", 
        max_length=350)
    
    serial = models.CharField(
        "Numero de serie", 
        max_length=150,
        unique=True)
    
    inventario = models.CharField(
        "Numero de inventario", 
        max_length=150,
        unique=True,
        primary_key=True)
    
    fecha_alta = models.DateField(
        "Fecha de alta del material", 
        auto_now=False, 
        auto_now_add=True)
    
    fecha_modificacion = models.DateField(
        "Fecha de modificación del material", 
        auto_now=True, 
        auto_now_add=False)
    
    disponible = models.BooleanField("Disponible", default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
    
    
    
class Clase(models.Model):
    
    imagen = models.ImageField(upload_to='clases/', null=True)
    
    nombre = models.CharField(
        "Nombre de la clase", 
        max_length=50)
    
    descripcion = models.CharField(
        "Descripción de la clase", 
        max_length=350)
    
    numero_clase = models.CharField(
        "Numero de clase", 
        max_length=150,
        unique=True,
        primary_key=True)
    
    fecha_alta = models.DateField(
        "Fecha de alta de la clase", 
        auto_now=False, 
        auto_now_add=True)
    
    fecha_modificacion = models.DateField(
        "Fecha de alta de la clase", 
        auto_now=True, 
        auto_now_add=False)
    
    disponible = models.BooleanField("Disponible", default=True)
    
    def __str__(self):
        return self.nombre + ' - ' + self.numero_clase
    
    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
    
    
    
class Equipo(models.Model):
    
    imagen = models.ImageField(upload_to='equipos/', null=True)
    
    nombre = models.CharField(
        "Nombre del equipo", 
        max_length=50)
    
    descripcion = models.CharField(
        "Descripción del equipo", 
        max_length=350)
    
    numero_clase = models.ForeignKey(
        Clase, 
        on_delete=models.CASCADE)
    
    numero_equipo = models.CharField(
        "Numero de equipo", 
        max_length=150,
        unique=True)
    
    fecha_alta = models.DateField(
        "Fecha de alta del equipo", 
        auto_now=False, 
        auto_now_add=True)
    
    fecha_modificacion = models.DateField(
        "Fecha de alta del equipo", 
        auto_now=True, 
        auto_now_add=False)
    
    disponible = models.BooleanField("Disponible", default=True)
    
    def __str__(self):
        return self.nombre + ' - ' + str(self.numero_clase) + ', equipo:' + self.numero_equipo
    


class Reservas(models.Model):
    
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="usuario_reserva")
    
    motivo_prestamo = models.CharField(
        "Motivo del préstamo", 
        max_length=250)
    
    fecha_reserva = models.DateField(
        "Fecha de reserva", 
        auto_now=False, 
        auto_now_add=True)
    
    fecha_devolucion = models.DateField(
        "Fecha de devolución")
    
    devuelto = models.BooleanField(
        "Ha sido devuelto")
    
    equipo = models.ManyToManyField(
        Equipo, 
        blank=True)
    
    clase = models.ManyToManyField(
        Clase, 
        blank=True)
    
    material = models.ManyToManyField(
        Material, 
        blank=True)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
