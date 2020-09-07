from django.db import models
from django.contrib.auth.models import User

class Perfil_empresa(models.Model):
    cnpj = models.CharField(max_length=255, null = False)
    cargo = models.CharField(max_length=255, null = False)
    telefone = models.CharField(max_length=255, null = False)
    cidade = models.CharField(max_length=255, null = False)
    empresa = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_empresa')

    @property
    def email_corporativo(self):
    	return self.empresa.email_corporativo

  #  def postar_vagas(self):
  #	return ...

#senha
#confirmar senha
#empresa
