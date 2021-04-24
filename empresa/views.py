from django.shortcuts import render, redirect,get_object_or_404
from .forms import SolicitacaoReltorioForm
from .models import SolicitacaoReltorio
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def solicitacaoRelatorioAdd(request):
    form = SolicitacaoReltorioForm()
    contexto = {'form': form}
    return render(request, 'empresa/solicitacao/form.html', contexto)

@login_required
def solicitacaoRelatorioSave(request):
    if request.method == 'POST':
        form = SolicitacaoReltorioForm(request.POST)
        contexto = {'form': form}
        if not form.is_valid():
            return render(request, 'empresa/solicitacao/form.html', contexto)
        form.save()
        # messages.success(request, 'Solicitação salva com Sucesso')
    return redirect('solicitacaolist')

@login_required
def solicitacaoRelatorioList(request):
    solicitacao = SolicitacaoReltorio.objects.order_by('-data_solicitacao')
    paginator = Paginator(solicitacao, 10)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    contexto = {
        'listar': receitas_por_pagina
    }
    return render(request,'empresa/solicitacao/list.html',contexto) 

@login_required
def solicitacaoRelatoriodel(request,solicitacao_id):
    solicitacao = get_object_or_404(SolicitacaoReltorio, pk=solicitacao_id)
    solicitacao.delete()
    return redirect('solicitacaolist')


