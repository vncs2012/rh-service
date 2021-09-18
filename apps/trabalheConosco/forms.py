from django import forms
from .models import Candidato,DadosPessoas,DadosEscolaridade


class CandidatoForm(forms.ModelForm):
    
    class Meta:
        model = Candidato
        fields="__all__"

class DadosPessoasForm(forms.ModelForm):
    
    class Meta:
        model = DadosPessoas
        fields="__all__"
        exclude=("id_candidato",)

class DadosEscolaridadeForm(forms.ModelForm):
    
    class Meta:
        model = DadosEscolaridade
        fields="__all__"
        exclude=("id_candidato",)

    