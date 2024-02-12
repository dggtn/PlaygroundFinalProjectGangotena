from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=120)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=10)
    apodo = models.CharField(max_length=10)
    pais = models.CharField(max_length=8)

class Comentarios(models.Model):
    autor = models.CharField(max_length=15)
    cuerpo = models.CharField(max_length=120)
