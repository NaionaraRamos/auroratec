from django import forms
from django.contrib.auth.models import User

class CadastrarUsuariaForm(forms.Form):

	nome = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	senha = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	linkedin = forms.CharField(required=True)
	cidade = forms.CharField(required=True)
	#foto

	def eh_valido(self):
	    valido = True
	    if not super(CadastrarUsuariaForm, self).eh_valido():
                self.indica_erro('Por favor, verifique os dados informados')
                valido = False

	    email_existe = User.objects.filter(email = self.data['email']).exists()
	    linkedin_existe = User.objects.filter(linkedin = self.data['linkedin']).exists()
	    telefone_existe = User.objects.filter(telefone = self.data['telefone']).exists()

	    if email_existe:
                self.indica_erro('Já existe uma usuária cadastrada com esse endereço de email.')
                valido = False

	    if linkedin_existe:
                self.indica_erro('Já existe uma usuária cadastrada com esse endereço de LinkedIn.')
                valido = False

	    if telefone_existe:
                self.indica_erro('Já existe uma usuária cadastrada com esse número de telefone.')
                valido = False

	def indica_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
