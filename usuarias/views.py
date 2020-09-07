from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis_usuarias.models import Perfil_usuaria
from usuarias.forms import CadastrarUsuariaForm

class CadastrarUsuariaView(View):

	template_name = 'cadastro.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = CadastrarUsuariaForm(request.POST)

		if form.is_valid():
			dados_form = form.data
			usuaria = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
			perfil = Perfil_usuaria(nome = dados_form['nome'],
					telefone = dados_form['telefone'],
					linkedin = dados_form['linkedin'],
					cidade = dados_form['cidade'],
					usuaria = usuaria)

			perfil.save()
			return redirect('chatbot')

		return render(request, self.template_name, {'form' : form })
