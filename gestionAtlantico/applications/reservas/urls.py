from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('materiales/', views.MaterialesListApiView.as_view()),
    path('clases/', views.ClasesListApiView.as_view()),
    path('equipos/', views.EquiposListApiView.as_view()),
    path('create/', views.ReservaCreateView.as_view()),
    path('creates/', views.ReservasAPIView.as_view()),
] 
