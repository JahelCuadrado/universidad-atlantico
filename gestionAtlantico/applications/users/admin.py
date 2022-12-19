from django.contrib import admin
from .models import User, Titulacion

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo',
        'tipo',
        'email_institucional',
    )
    
    
    def nombre_completo(self, obj):
        return obj.first_name + ' ' + obj.last_name

class TitulacionAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'duracion_titulo',
    )
    
    def duracion_titulo(self, obj):
        return str(obj.duracion) + ' años'

admin.site.register(User, UserAdmin)
admin.site.register(Titulacion, TitulacionAdmin)