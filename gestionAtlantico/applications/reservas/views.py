from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
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