from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=120)