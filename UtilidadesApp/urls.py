from django.urls import path
from UtilidadesApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pares', views.pares, name="pares"),
   
]