from django.contrib import admin
from .models import Material, Clase, Equipo, Reservas
from .serializers import ReservasSerializer
from django.contrib import messages

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
    )
    filter_horizontal = ('equipo', 'clase', 'material',)
    
    def delete_model(self, request, obj):        
        disponibles(obj.id)   
        obj.delete()
        
    def delete_queryset(self, request, queryset):
        for reserva in queryset:
            disponibles(reserva.id)
        queryset.delete()
        
    def save_model(self, request, obj, form, change):
        serializer = ReservasSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            pass
        else:
            self.message_user(request, 'Error', messages.ERROR)
    
    
def disponibles(id):
        reserva = Reservas.objects.get(id=id)
        equipos = reserva.equipo.all()
        materiales = reserva.material.all()
        clases = reserva.clase.all()
                
        for equipo in equipos:
            equipo.disponible = True
            equipo.save()
                    
        for material in materiales:
            material.disponible = True
            material.save()
                
        for clase in clases:
            clase.disponible = True
            clase.save()


       


admin.site.register(Material, MaterialAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Reservas, ReservasAdmin)