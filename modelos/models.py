from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=10)
    apodo = models.CharField(max_length=10)
    pais = models.CharField(max_length=20)
    email = models.EmailField()
    
class Post(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cuerpo = models.CharField(max_length=5000)



class Comentarios(models.Model):
    autor = models.CharField(max_length=15)
    cuerpo = models.CharField(max_length=120)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Avatar(models.Model):
     user= models.OneToOneField(User, on_delete = models.CASCADE)
     def __str__(self):
         return f"{self.user} - {self.imagen}"
     
