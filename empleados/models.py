from django.db import models

# Create your models here.

class Empleado(models.Model):
    TIPOS_EMPLEADOS = (
        ('BASE', 'PERSONAL BASIFICADO'),
        ('CONF', 'PERSONAL DE CONFIANZA'),
    )
    numero_empleado = models.CharField(max_length=10)
    datos = models.ForeignKey('catalogos.Persona')
    fecha_ingreso = models.DateTimeField()
    clave_plaza = models.ForeignKey('catalogos.plaza')
    adscripcion = models.ForeignKey('catalogos.Adscripcion')
    puesto = models.CharField(max_length=40)
