from django.urls import path
from . import views

# Esto crea el namespace para que luego uses 'calendario:calendario'
app_name = "calendario"

urlpatterns = [
    path('<str:fecha>/', views.calendario, name='calendario'),
]