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
		fields = (
			'id',
			'usuario',
			'motivo_prestamo',
			'fecha_devolucion',
			'devuelto',
			'equipo',
			'clase',
			'material',
        	)
  
	def validate(self, data):
     
		equipos = data['equipo']
		for equipo in equipos:
			equipo_obj = Equipo.objects.get(pk=equipo.id)
			if equipo_obj.disponible:
				pass
			else:
				raise serializers.ValidationError('No se puede reservar un objeto que no está disponible')

		clases = data['clase']
		for clase in clases:
			clase_obj = Clase.objects.get(pk=clase.numero_clase)
			if clase_obj.disponible:
				pass
			else:
				raise serializers.ValidationError('No se puede reservar un objeto que no está disponible')

		materiales = data['material']
		for material in materiales:
			material_obj = Material.objects.get(pk=material.inventario)
			if material_obj.disponible:
				pass
			else:
				raise serializers.ValidationError('No se puede reservar un objeto que no está disponible')


		return data
