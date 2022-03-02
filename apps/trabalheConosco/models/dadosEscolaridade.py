from django.db import models
from .candidato import Candidato
from trabalheConosco.utils import STATUS_ESCOLARIDADE

class DadosEscolaridade(models.Model):
    descricao = models.CharField("Curso/Escola", max_length=150)
    status = models.IntegerField('Escolaridade:', choices=STATUS_ESCOLARIDADE)
    data_inicio = models.DateField("Data de inicio", auto_now=False, auto_now_add=False)
    data_fim = models.DateField("Previsão termino/data termino", auto_now=False, auto_now_add=False)
    id_candidato = models.ForeignKey(Candidato, verbose_name="Candidato", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DadosEscolaridade"
        verbose_name_plural = "DadosEscolaridades"

    def get_absolute_url(self):
        return reverse("DadosEscolaridade_detail", kwargs={"pk": self.pk})