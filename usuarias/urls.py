from django.urls import path
from usuarias.views import CadastrarUsuariaView
from django.contrib.auth.views import LoginView, LogoutView
from empresas import views 

urlpatterns = [
    path('cadastro', CadastrarUsuariaView.as_view(), name="cadastro"),
    path('login', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout')
]

