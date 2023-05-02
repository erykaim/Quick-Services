from django.db import models

# Create your models here.
#esto crea una tabla llamada persona
class persona(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_doc = models.CharField(max_length=255)
    documento = models.PositiveSmallIntegerField()
    correo = models.CharField(max_length=255)
    telefono = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

class Meta:
        app_label = 'usuarios'