from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, default=None, blank=True)
    cuerpo = models.CharField(max_length=5000)

class Comentarios(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.CharField(max_length=120)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)