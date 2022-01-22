from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory

from .models import Candidato,DadosPessoas,DadosEscolaridade,DadosProfissionais,vagasCandidato


class CandidatoForm(forms.ModelForm):
    
    class Meta:
        model = Candidato
        fields="__all__"

class DadosPessoasForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    class Meta:
        model = DadosPessoas
        fields="__all__"
        exclude=("id_candidato",)

class DadosEscolaridadeForm(forms.ModelForm):
    data_inicio = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    data_fim = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    
    class Meta:
        model = DadosEscolaridade
        fields="__all__"
        exclude=("id_candidato",)


class DadosProfissionaisForm(forms.ModelForm):
    
    data_admissao = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    data_demissao = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    class Meta:
        model = DadosProfissionais
        fields="__all__"
        exclude=("id_candidato",)

class DadosVagasForm(forms.ModelForm):
  
    class Meta:
        model = vagasCandidato
        fields="__all__"
        exclude=("id_candidato",)

vagasFormSet = inlineformset_factory(Candidato,vagasCandidato, form=DadosVagasForm, fields=['id_vaga', ], extra=1,can_delete=True)

EscolaridadeFormSet = inlineformset_factory(Candidato,DadosEscolaridade, form=DadosEscolaridadeForm,
fields=['descricao','status','data_inicio','data_fim',],
 extra=1,can_delete=False)
 
ProfissionaisFormSet = inlineformset_factory(Candidato,DadosProfissionais, form=DadosProfissionaisForm,
fields=['cargo','Empresa','data_admissao','data_demissao','descricao',],
 extra=1,can_delete=False)