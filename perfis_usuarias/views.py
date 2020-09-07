from django.shortcuts import render;

def home(request):
    return render(request, 'home.html');

def login(request):
    return render(request, 'login.html');

def cadastro(request):
    return render(request, 'cadastro.html');

def cadastro_empresas(request):
    return render(request, 'cadastro-empresas.html');

def candidaturas(request):
    return render(request, 'candidaturas.html');

def chatbot(request):
    return render(request, 'chatbot.html');

def premium(request):
    return render(request, 'premium.html');

def resultado_de_competencias(request):
    return render(request, 'resultado-de-competencias.html');

def vagas(request):
    return render(request, 'vagas.html');

def vagas_inscricao_realizada(request):
    return render(request, 'vagas-inscricao-realizada.html');
