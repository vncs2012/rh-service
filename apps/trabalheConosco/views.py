from .models import vagasCandidato,DadosPessoas,Candidato
from django.forms.models import inlineformset_factory
from .forms import CandidatoForm, DadosEscolaridadeForm, DadosPessoasForm, DadosProfissionaisForm, DadosVagasForm, vagasFormSet
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
        ('escolaridade',DadosEscolaridadeForm),
        ('profissional',DadosProfissionaisForm),
        ('vagas',vagasFormSet),

    ]

    def done(self, form_list, form_dict, **kwargs):
        print('entrou aqui')
        # print(form_dict)
        candidato = form_dict['candidato'].save(commit=False)
        # print(candidato)
        if(candidato):
           
            dadosPessoas = form_dict['dadosPessoas'].save(commit=False)
            dadosEscolaridade = form_dict['escolaridade'].save(commit=False)
            DadosProfissionais = form_dict['profissional'].save(commit=False)

            saveVagas(form_dict['vagas'],candidato)
            
            dadosPessoas.id_candidato = candidato
            dadosEscolaridade.id_candidato = candidato
            DadosProfissionais.id_candidato = candidato
    
            # DadosVagas.id_candidato = candidato

            if(dadosPessoas.id_candidato):
                candidato.save()
                dadosPessoas.save()
                dadosEscolaridade.save()
                DadosProfissionais.save()
                # DadosVagas.save()

                print('Salvo com Sucesso')
        return render(self.request, 'trabalheConosco/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
    
    def saveForms():
        return True

def saveVagas(dadosVagas,candidato):
    formset = vagasFormSet(dadosVagas,instance=candidato)
    print(formset)
    instances = formset.save(commit=False)
    for instance in instances:
        instance.save()
    