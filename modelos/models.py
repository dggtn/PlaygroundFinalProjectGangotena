from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=120)
    cuerpo = models.CharField(max_length=5000)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=10)
    apodo = models.CharField(max_length=10)
    pais = models.CharField(max_length=20)
    email = models.EmailField(default = "")

class Comentarios(models.Model):
    autor = models.CharField(max_length=15)
    cuerpo = models.CharField(max_length=120)
class Avatar(models.Model):
     user= models.OneToOneField(User, on_delete = models.CASCADE)
     def __str__(self):
         return f"{self.user} - {self.imagen}"