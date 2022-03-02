from django.contrib import messages
from recrutamentoSelecao.models import Entrevista
from .models import vagasCandidato, DadosPessoas, Candidato
from django.forms.models import inlineformset_factory
from .forms import CandidatoForm, EscolaridadeFormSet, DadosPessoasForm, ProfissionaisFormSet, vagasFormSet
from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView

# Create your views here.


def home(request):
    return render(request, 'trabalheConosco/home.html')


class cadastro(SessionWizardView):
    template_name = "trabalheConosco/cadastro.html"

    form_list = [
        ('candidato', CandidatoForm),
        ('dadosPessoas', DadosPessoasForm),
        ('escolaridade', EscolaridadeFormSet),
        ('profissional', ProfissionaisFormSet),
        ('vagas', vagasFormSet),
    ]

    def done(self, form_list, form_dict, **kwargs):
        candidato = form_dict['candidato'].save(commit=False)
        if(candidato):
            candidato.save()

            dadosPessoas = form_dict['dadosPessoas'].save(commit=False)
            dadosPessoas.id_candidato = candidato

            if(dadosPessoas.id_candidato):
                dadosPessoas.save()
                saveFormSet(form_dict['escolaridade'], candidato)
                saveFormSet(form_dict['profissional'], candidato)
                saveFormSet(form_dict['vagas'], candidato)

                print('Salvo com Sucesso')
        return render(self.request, 'trabalheConosco/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)


def saveFormSet(formSet, candidato):
    for form in formSet:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id_candidato = candidato
            obj.save()


def saveProximaFaseEntrevista(request, obj):
    for item in obj:
        try:
            e = Entrevista()
            e.id_candidato = item
            e.save()
            messages.success(
                request, f'Candidato {item.nome} movido para entrevista', fail_silently=True)
        except e:
            messages.error(
                request, f'Erro ao movimentação para entrevista o candidato {item.nome}')

        print(item.id, item.nome, item.cpf)
