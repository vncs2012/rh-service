from django import forms
from django.forms.models import inlineformset_factory

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




vagasFormSet = inlineformset_factory(Candidato,vagasCandidato, form=DadosVagasForm, fields=['id_vaga', ], extra=3)
