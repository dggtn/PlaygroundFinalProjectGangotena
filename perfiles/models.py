from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  apodo = models.CharField(max_length=10)
  pais = models.CharField(max_length=20)
  avatar = models.ImageField(upload_to='avatares/', null=True, default=None, blank=True)