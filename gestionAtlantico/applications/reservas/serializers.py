from rest_framework import serializers
from .models import Material, Clase, Equipo, Reservas


class MaterialSerializer(serializers.ModelSerializer):
		class Meta:
				model = Material
				fields = ('__all__')
    
    
class ClaseSerializer(serializers.ModelSerializer):
		class Meta:
				model = Clase
				fields = ('__all__')
    
    
class EquipoSerializer(serializers.ModelSerializer):
		class Meta:
				model = Equipo
				fields = ('__all__')
    
    
class ReservasSerializer(serializers.ModelSerializer):
		class Meta:
				model = Reservas
				fields = ('__all__')