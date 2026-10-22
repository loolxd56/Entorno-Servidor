from django.urls import path, include
from . import views

app_name = "practica"
urlpatterns = [
 path('', views.homepage, name='homepage'),
]
