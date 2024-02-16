from django.test import TestCase,Client

from django.urls import reverse
from django.contrib.auth.models import User

from modelos.models import Usuarios


class RegistrarTestCase(TestCase):
   def setUp(self):
        self.usuario= Usuarios.objects.create(nombre='Juan',apellido='Perez',apodo="juani",pais="Ecuador",email="jp@gmail.com")
        self.url = reverse('EliminarUusario', args=[self.usuario.nombre])
    
   def test_eliminar_usuario(self):
       respuesta = self.client.get(self.url)
       self.assertEqual(respuesta.status_code, 200)
       self.assertTemplateUsed(respuesta, 'leerUsuarios.html')
       self.assertQuerysetEqual(Usuarios.objects.all(),[])
   