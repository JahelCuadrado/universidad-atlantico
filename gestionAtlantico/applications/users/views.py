from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import UserRegisterSerializer, UserTitulacionSerializer
from rest_framework.response import Response
from rest_framework import status
from applications.users.models import Titulacion
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


# Create your views here.
class RegisterView(APIView):
	def post(self, request):
		serializer = UserRegisterSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
     
		print('Registrando...')
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TitulacionView(ListAPIView):
    serializer_class = UserTitulacionSerializer
    def get_queryset(self):
        return Titulacion.objects.all()
    
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)