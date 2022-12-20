from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import MaterialSerializer, ClaseSerializer, EquipoSerializer, ReservasSerializer
from .models import Material, Clase, Equipo, Reservas

# Create your views here.
class MaterialesListApiView(ListAPIView):
		serializer_class = MaterialSerializer
		def get_queryset(self):
				return Material.objects.all()

class ClasesListApiView(ListAPIView):
		serializer_class = ClaseSerializer
		def get_queryset(self):
				return Clase.objects.all()

class EquiposListApiView(ListAPIView):
		serializer_class = EquipoSerializer
		def get_queryset(self):
				return Equipo.objects.all()

class ReservaCreateView(CreateAPIView):
		serializer_class = ReservasSerializer
		def get_queryset(self):
				return Reservas.objects.all()