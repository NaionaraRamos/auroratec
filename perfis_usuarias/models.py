from django.db import models
from django.contrib.auth.models import User

class Perfil_usuaria(models.Model):
    nome = models.CharField(max_length=255, null = False)
    telefone = models.CharField(max_length=255, null = False)
    linkedin = models.CharField(max_length=255, null = False)
    cidade = models.CharField(max_length=255, null = False)
    usuaria = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuaria')

    @property
    def email(self):
    	return self.usuaria.email
