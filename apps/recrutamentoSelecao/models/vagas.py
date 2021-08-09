from django.db import models
from .cargos import Cargos


class Vagas(models.Model):
    cargo = models.OneToOneField(
        Cargos, verbose_name="Cargo", on_delete=models.CASCADE) 
    descricao = models.TextField("Descrição da Vaga: ")
    status = models.BooleanField("Status :", default=True)

    class Meta:
        verbose_name = "Vagas"
        verbose_name_plural = "Cadastro de Vagas"

    def __str__(self):
        return f'{str(self.cargo)}'

    def get_absolute_url(self):
        return reverse("Vagas_detail", kwargs={"pk": self.pk})