from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('titulaciones/', views.TitulacionView.as_view(), name='titulaciones'),
    path('me/', views.UserView.as_view(), name='user'),
]
