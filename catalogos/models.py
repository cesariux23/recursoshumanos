from django.db import models

# Create your models here

class Persona(models.Model):
    rfc = models.CharField(max_length=13)
    curp = models.CharField(max_length=18)
    nombre = models.CharField(max_length=80)
    paterno = models.CharField(max_length=80)
    materno = models.CharField(max_length=80)

class Adscripcion(models.Model):
    unidad = models.CharField(max_length=4)
    subunidad = models.CharField(max_length=4)
    nombre = models.CharField(max_length=100)

class Plaza(models.Model):
    clave = models.CharField(max_length=8, primary_key=True)
    nivel = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=100)
