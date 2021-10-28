from django.db import models

# Create your models here.

#agregar relacion plantel/abonado,abonado/equipamiento, plantel/equipamiento 
class abonados(models.Model):
    nombre_abonado = models.CharField(max_length=30, null=True)
    numero_telefono = models.CharField(max_length=7, primary_key=True) #quitar null luego y agregar primarykeytrue
    direccion_abonado = models.CharField(max_length=30, null=True)
    observacion_abonado = models.CharField(max_length=50, null=True)

class equipamiento(models.Model):
    nombre_equipamiento = models.CharField(max_length=20, null=True)
    ubicacion_puerto = models.CharField(max_length=3, null=True)
    numero_telefono = models.ForeignKey(abonados, on_delete= models.CASCADE)

class plantel(models.Model):
    condicion_plantel = models.CharField(max_length=10, null=True)
    par_numero = models.CharField(max_length=4, null=True)
    numero_telefono = models.ForeignKey(abonados, on_delete= models.CASCADE)

#agregar relacion plantel/abonado,abonado/equipamiento, plantel/equipamiento 
 