from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis_empresas.models import Perfil_empresa
from empresas.forms import CadastrarEmpresaForm

class CadastrarEmpresaView(View):

	template_name = 'cadastro-empresas.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = CadastrarEmpresaForm(request.POST)

		if form.is_valid():
			dados_form = form.data
			empresa = User.objects.create_user(dados_form['empresa'], dados_form['email_corporativo'], dados_form['senha']) 
			perfil_empresa = Perfil_empresa(nome = dados_form['empresa'],
							cnpj = dados_form['cnpj'],
							telefone = dados_form['telefone'],
							cidade = dados_form['cidade'],
							empresa = empresa)
			perfil_empresa.save()
			return redirect('dashboard_empresas')

		return render(request, self.template_name, {'form' : form})

