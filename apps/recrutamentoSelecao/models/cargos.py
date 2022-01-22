from django.db import models
from .departamento import Departamento

class Cargos(models.Model):
    nome = models.CharField("Cargo", max_length=50)
    salario_base = models.CharField("Salario Base", max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    status = models.BooleanField("Cargo Ativo ?")

    class Meta:
        verbose_name = "Cargos"
        verbose_name_plural = "Cadastro de Cargos"

    def __str__(self):
        return f'{self.nome}'

    def get_absolute_url(self):
        return reverse("Cargos_detail", kwargs={"pk": self.pk})