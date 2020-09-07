from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('empresas', views.cadastro_empresas, name='cadastro_empresas'),
	path('candidaturas', views.candidaturas, name='candidaturas'),
	path('chatbot', views.chatbot, name='chatbot'),
	path('premium', views.premium, name='premium'),
	path('resultado_de_competencias', views.resultado_de_competencias, name='resultado_de_competencias'),
	path('vagas', views.vagas, name='vagas'),
	path('vagas_inscricao_realizada', views.vagas_inscricao_realizada, name='vagas_inscricao_realizada'),
]
