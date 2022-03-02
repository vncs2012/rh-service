from audioop import reverse
from django.db import models
from trabalheConosco.models.candidato import Candidato


class Entrevista(models.Model):
    id_candidato = models.ForeignKey(Candidato, verbose_name="Candidato", on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Entrevista"
        verbose_name_plural = "Entrevista"

    def __str__(self):
        return str(self.id_candidato)

    def get_absolute_url(self):
        return reverse("entrevista_detail", kwargs={"pk": self.id_candidato})
