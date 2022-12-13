from django.contrib import admin
from .models import Material, Clase, Equipo, Reservas

# Register your models here.
admin.site.register(Material)
admin.site.register(Clase)
admin.site.register(Equipo)
admin.site.register(Reservas)