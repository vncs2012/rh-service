from django import forms
from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput

from .models import Empresa, SolicitacaoReltorio


class EmpresaForm(forms.ModelForm):
    # contato = forms.CharField(widget=BRPhoneNumberInput())
    class Meta:
        model = Empresa
        fields="__all__"


class SolicitacaoReltorioForm(forms.ModelForm):
    preco = forms.DecimalField(disabled=True,required=False)
    quantidade_restante = forms.IntegerField(disabled=True,required=False)

    class Meta:
        model = SolicitacaoReltorio
        fields ="__all__"

    def clean(self):
        quantidade_solicitada = self.cleaned_data.get('quantidade_solicitada')
        preco = self.cleaned_data.get('preco')
        self.cleaned_data['preco'] = quantidade_solicitada*150
        self.cleaned_data['quantidade_restante'] = quantidade_solicitada

        return self.cleaned_data
