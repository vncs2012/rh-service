from django.db import models
from .candidato import Candidato
from trabalheConosco.utils import TP_ESCOLARIDADE, SEXO, TP_ESTADO_CIVIL


class DadosPessoas(models.Model):
    rg = models.CharField("RG:", max_length=164)
    sexo = models.CharField('SEXO:', choices=SEXO, max_length=1)
    estado_civil = models.IntegerField('Estado Civil:', choices=TP_ESTADO_CIVIL)
    escolaridade = models.IntegerField('Escolaridade:', choices=TP_ESCOLARIDADE)
    contato = models.CharField("Numero para contato", max_length=12)
    nome_mae = models.CharField("Nome da Mãe:", max_length=164)
    nome_pai = models.CharField("Nome do Pai:", max_length=164)
    endereco = models.CharField("Endereco:", max_length=256)
    cidade = models.CharField("Cidade:", max_length=100)
    estado = models.CharField("Estado:", max_length=35)
    id_candidato = models.ForeignKey(Candidato, verbose_name="Candidato", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DadosPessoas"
        verbose_name_plural = "Dados Pessoass"

    def get_absolute_url(self):
        return reverse("DadosPessoas_detail", kwargs={"pk": self.pk})