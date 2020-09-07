from django.urls import path
from empresas.views import CadastrarEmpresaView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('cadastro_empresas', CadastrarEmpresaView.as_view(), name='cadastro_empresas'),

#DESCOMENTAR QUANDO HOUVER PÁGINA DE LOGIN DA EMPRESA
#    path('login_empresa/', LoginView.as_view(template_name = 'login_empresa.html'), name = 'login'),
#    path('logout/', LogoutView.as_view(), name = 'logout')
]
