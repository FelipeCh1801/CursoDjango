from django.db import models

class Carreras(models.Model):
    id_carrera=models.IntegerField
    pais=models.CharField(max_length=200)
    circuito=models.CharField(max_length=200)

    def __str__(self):
        return self.pais
# Create your models here.
