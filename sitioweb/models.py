from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tecnico(models.Model):
	nombre=models.CharField(max_length=100)
	
	def __str__ (self):
	    return self.nombre

class add_cli(models.Model):
	nombre=models.CharField(max_length=100)
	direccion=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=50)
	comuna=models.CharField(max_length=50)
	telefono=models.IntegerField()
	correo=models.CharField(max_length=50)
	tecnico=models.CharField(max_length=50, default='SOME STRING')

	def __str__ (self):
	    return self.nombre

class add_OrdenTrabajo(models.Model):
	cliente=models.CharField(max_length=100)
	fecha=models.DateField(null=False, max_length=50)
	hora_ini=models.CharField(max_length=50)
	hora_ter=models.CharField(max_length=50)
	id_ascen=models.CharField(max_length=5)
	modelo=models.CharField(max_length=10)
	fallas=models.CharField(max_length=100)
	reparacion=models.CharField(max_length=100)
	pieza_cam=models.CharField(max_length=100)
	nom_trab=models.CharField(max_length=100)

	def __str__ (self):
	    return self.cliente

	    # usuario






