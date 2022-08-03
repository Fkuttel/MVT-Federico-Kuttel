from django.db import models

# Create your models here.

    
class Te(models.Model):
    nombre=models.CharField(blank=True, max_length=30)
    aroma=models.CharField(blank=True, max_length=30)
    
    def __str__(self):
        return f"La infusion que buscaste se llama {self.nombre}"