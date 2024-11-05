from django.db import models # type: ignore

# Create your models here.
class Seminario(models.Model):
    nombrePersona = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaSeminario = models.DateField()
    empresaInstitucion = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=200)