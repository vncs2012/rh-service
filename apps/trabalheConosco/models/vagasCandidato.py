from django.db import models
from .candidato import Candidato
from recrutamentoSelecao.models.vagas import Vagas

class vagasCandidato(models.Model):

    id_candidato = models.ForeignKey(Candidato, verbose_name="Candidato", on_delete=models.CASCADE)
    id_vaga = models.ForeignKey(Vagas, verbose_name="Vagas Disponivel", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "vagasCandidato"
        verbose_name_plural = "Vagas candidato"

    def get_absolute_url(self):
        return reverse("vagasCandidato_detail", kwargs={"pk": self.pk})