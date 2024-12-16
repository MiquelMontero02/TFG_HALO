from django.db import models

class Formulario(models.Model):
    titulo=models.CharField(max_length=255)
    step=models.IntegerField()
