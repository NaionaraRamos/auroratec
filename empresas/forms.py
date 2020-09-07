from django import forms
from django.contrib.auth.models import User

class CadastrarEmpresaForm(forms.Form):

	cnpj = forms.CharField(required=True)
	cargo = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	cidade = forms.CharField(required=True)
	empresa = forms.CharField(required=True)
	email_corporativo = forms.EmailField(required=True)
	senha = forms.CharField(required=True)

	def eh_valido(self):
	    valido = True
	    if not super(CadastrarEmpresaForm, self).eh_valido():
                self.indica_erro('Por favor, verifique os dados informados.')
                valido = False

                empresa_existe = User.objects.filter(username = self.data['empresa']).exists()
                email_corporativo_existe = User.objects.filter(email = self.data['email_corporativo']).exists()

	    if empresa_existe:
                self.indica_erro('Empresa já existente')
                valido = False

	    if email_corporativo_existe:
                self.indica_erro('Já existe uma empresa cadastrada com esse email corporativo.')
                valido = False
 
	    return valido

	def indica_erro(self, message):
            errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
            errors.append(message)
