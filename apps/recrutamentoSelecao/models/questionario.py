from django.db import models
from .cargos import Cargos

class Questionario(models.Model):
    cargo = models.ForeignKey(Cargos, verbose_name="Cargo", on_delete=models.CASCADE, null=True, blank=True)
    trabalhe_conosco = models.BooleanField("Padrão do trabalhe Conosco?")

    class Meta:
        verbose_name = "Questionario"
        verbose_name_plural = "Cadastro de Questionario"

    def __str__(self):
        return str(self.cargo)

    def get_absolute_url(self):
        return reverse("Questionario_detail", kwargs={"pk": self.pk})