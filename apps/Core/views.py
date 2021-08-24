from . import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import PerguntaQuestionario
from empresa.models import EmpresaUsuarios, Empresa
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django.db import transaction


def index(request):
    return render(request, 'trabalheConosco/home.html')


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


@login_required
def create_user(request):
    form = UserCreationForm()
    contexto = {
        'form': form
    }
    if request.method == 'POST':
        createUser = UserCreationForm(request.POST)
        contexto = {
            'form': createUser
        }
        if not createUser.is_valid():
            return render(request, 'usuario/create.html', contexto)
        with transaction.atomic():
            usersave = createUser.save()
            empresa = Empresa.objects.filter(user_admin=request.user).first()
            # usersave = User.objects.filter(username==createUser.username).first()
            empresa_user = EmpresaUsuarios()
            empresa_user.id_empresa = empresa
            empresa_user.user = usersave
            empresa_user.save()

        # Criar rotina para vincular o novo usuario com a empresa/Consultor(Coach)
        return redirect('index')

    return render(request, 'usuario/create.html', contexto)


@login_required
def list_user(request):
    empresa = Empresa.objects.filter(user_admin=request.user).first()
    users = EmpresaUsuarios.objects.filter(id_empresa=empresa).all()
    contexto = {
        'listar': users
    }
    return render(request, 'usuario/list.html', contexto)

def del_user(request,id_user):
    pass



@login_required
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
