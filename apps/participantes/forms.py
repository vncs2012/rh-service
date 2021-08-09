from django import forms
from .models import Participantes



class ParticipantesForm(forms.ModelForm):
    
    class Meta:
        model = Participantes
        fields="__all__"
        exclude=('foto','participante','empresa')