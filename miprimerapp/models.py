
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Cafe(models.Model):
    nombre=models.CharField(blank=True, max_length=30)
    tostado=models.CharField(blank=True, max_length=30)
    descripcion = RichTextField(null=True)
    cuerpo=models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"El cafe que buscaste se llama {self.nombre}"

