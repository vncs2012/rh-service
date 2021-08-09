from django.db import models
from .candidato import Candidato

class QuestionarioPadrao(models.Model):
    """Buscar questionario do recrutamentoSelecao -> questionario"""
    id_candidato = models.ForeignKey(
        Candidato, verbose_name="Candidato", on_delete=models.CASCADE)
    id_pergunta = models.CharField("", max_length=1)
    id_resposta = models.CharField("", max_length=1)

    class Meta:
        verbose_name = "QuestionarioPadrao"
        verbose_name_plural = "Questionario "

    def get_absolute_url(self):
        return reverse("QuestionarioPadrao_detail", kwargs={"pk": self.pk})
