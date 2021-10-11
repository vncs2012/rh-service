from django.db import models
from .candidato import Candidato

class DadosProfissionais(models.Model):
    cargo = models.CharField("Cargo de atuação", max_length=50)
    Empresa = models.CharField("Empresa", max_length=50)
    data_admissao = models.DateField(
        "Data admissao", auto_now=False, auto_now_add=False)
    data_demissao = models.DateField(
        "Data Demissao", auto_now=False, auto_now_add=False)
    descricao = models.TextField("descriçao de atividade:")
    id_candidato = models.ForeignKey(Candidato, verbose_name="Candidato", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DadosProfisional"
        verbose_name_plural = "DadosProfissionais"

    def get_absolute_url(self):
        return reverse("DadosProfisional_detail", kwargs={"pk": self.pk})