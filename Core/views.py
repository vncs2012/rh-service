from . import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import PerguntaQuestionario
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    """ Realiza uma Pessoa no Sistema"""
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']

        if campo_vazio(username) or campo_vazio(senha):
            messages.error(request, 'E-mail ou senha não pode ficar em Branco')
            return redirect('login')

        usuario = auth.authenticate(request, username=username, password=senha)

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Login realizado com Sucesso')
            return redirect('index')
        else:
            print('Usuario ou Senha incorreto')
            messages.error(request, 'Usuario ou Senha incorreto')

    return render(request, 'usuario/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()


def verifique_user_existe(email, nome=None):
    if nome:
        return User.objects.filter(email=email, username=nome).exists()
    return User.objects.filter(email=email).exists()


def verifica_senhas_sao_iguais(senha, senha2):
    return senha != senha2


def questionario(request):
    perguntas = PerguntaQuestionario.objects.order_by('nu_pergunta').all()
    dados = {
        'perguntas': perguntas
    }
    return render(request, 'questionario.html', dados)
