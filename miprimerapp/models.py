
from django.db import models

# Create your models here.
class Cafe(models.Model):
    nombre=models.CharField(blank=True, max_length=30)
    tostado=models.CharField(blank=True, max_length=30)
    cuerpo=models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"El cafe que buscaste se llama {self.nombre}"

