from django.urls import path
from . import views

urlpatterns = [
	path('dashboard_empresas', views.dashboard_empresas, name='dashboard_empresas')
	#INSERIR VIEW postar_vaga QUANDO O TEMPLATE ESTIVER PRONTO.
	#INSERIR VIEW consultar_candidaturas
]
