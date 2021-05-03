from django.shortcuts import render, redirect
from .forms import ParticipantesForm
from .models import Participantes
from empresa.models import Empresa, EmpresaUsuarios
from django.contrib.auth.decorators import login_required

# Create your views here.


def questionario_paricipante(request):
    pass


def paricipante_edit(request):
    return render(request, 'participante/verificarDados.html')


@login_required
def paricipante_list(request):
    empresa = get_empresa(request.user)
    participantes = Participantes.objects.filter(empresa=empresa).all()
    contexto = {
        'listar': participantes
    }

    return render(request, 'participante/list.html', contexto)


@login_required
def create_participante(request):
    form = ParticipantesForm
    context = {
        'form': form
    }
    return render(request, 'participante/form.html', context)


@login_required
def save(request):
    if request.method == 'POST':
        form = ParticipantesForm(request.POST)
        empresa = get_empresa(request.user)
        contexto = {'form': form}
        if not form.is_valid():
            return render(request, 'participante/form.html', contexto)
        save = form.save(commit=False)
        save.empresa = empresa
        save.save()

    return redirect('paricipante_list')


def get_empresa(user):
    empresa = Empresa.objects.filter(user_admin=user).first()
    if(empresa):
        empresa = EmpresaUsuarios.objects.filter(
            user=user).first().id_empresa
    return empresa
