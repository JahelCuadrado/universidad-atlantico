from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MaterialSerializer, ClaseSerializer, EquipoSerializer, ReservasSerializer
from .models import Material, Clase, Equipo, Reservas
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MaterialesListApiView(ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = MaterialSerializer
	def get_queryset(self):
		return Material.objects.all()



class ClasesListApiView(ListAPIView):
		permission_classes = [IsAuthenticated]
		serializer_class = ClaseSerializer
		def get_queryset(self):
			return Clase.objects.all()



class EquiposListApiView(ListAPIView):
		permission_classes = [IsAuthenticated]
		serializer_class = EquipoSerializer
		def get_queryset(self):
			return Equipo.objects.all()



class ReservaCreateView(CreateAPIView):
		permission_classes = [IsAuthenticated]
		serializer_class = ReservasSerializer
		def get_queryset(self):
			return Reservas.objects.all()



class ReservasAPIView(APIView):
    def post(self, request):
        serializer = ReservasSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            reserva = serializer.save()
            disponibles(reserva.id)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
        
def disponibles(id):
    reserva = Reservas.objects.get(id=id)
    equipos = reserva.equipo.all()
    materiales = reserva.material.all()
    clases = reserva.clase.all()
    
    for equipo in equipos:
        equipo.disponible = False
        equipo.save()
        
    for material in materiales:
        material.disponible = False
        material.save()
    
    for clase in clases:
        clase.disponible = False
        clase.save()