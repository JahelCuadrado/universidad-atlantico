from django.contrib import admin
from .models import Material, Clase, Equipo, Reservas

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'inventario',
        'nombre',
        'serial',
        'fecha_alta',
        'fecha_modificacion',
        'disponible',
    )
    
class ClaseAdmin(admin.ModelAdmin):
    list_display = (
        'numero_clase',
        'nombre',
        'fecha_alta',
        'fecha_modificacion',
        'disponible',
    )
    
class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'numero_clase',
        'numero_equipo',
        'fecha_alta',
        'fecha_modificacion',
        'disponible',
    )
    
class ReservasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'fecha_reserva',
        'fecha_devolucion',
        'devuelto',
        'equipo',
        'clase',
        'material',
    )

admin.site.register(Material, MaterialAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Reservas, ReservasAdmin)