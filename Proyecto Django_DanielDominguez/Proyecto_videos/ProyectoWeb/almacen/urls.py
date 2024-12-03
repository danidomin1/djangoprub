# urls.py en la aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('', views.almacen, name="Almacen"),
]
