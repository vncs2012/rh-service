from django.db import models


class Departamento(models.Model):
    nome = models.CharField("Departemento", max_length=128)
    status = models.BooleanField()

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Cadastro de Departamentos"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Departamento_detail", kwargs={"pk": self.pk})