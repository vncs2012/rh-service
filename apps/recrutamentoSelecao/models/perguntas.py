from django.db import models
from .questionario import Questionario

class Perguntas(models.Model):
    questionario_id = models.ForeignKey(Questionario, verbose_name="Questionario", on_delete=models.CASCADE)
    descricao = models.CharField("Pergunta", max_length=256)
    resposta1 = models.CharField(
        "resposta 1", max_length=256, null=True, blank=True)
    resposta2 = models.CharField(
        "resposta 2", max_length=256, null=True, blank=True)
    resposta3 = models.CharField(
        "resposta 5", max_length=256, null=True, blank=True)
    resposta4 = models.CharField(
        "resposta 4", max_length=256, null=True, blank=True)
    resposta5 = models.CharField(
        "resposta 5", max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = "Perguntas"
        verbose_name_plural = "Cadastro de Perguntas"

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("Perguntas_detail", kwargs={"pk": self.pk})