from django.db import models
from django.urls import reverse

class Candidato(models.Model):
    cpf = models.CharField("CPF:", max_length=14, unique=True)
    email = models.EmailField("Digite seu E-mail:", max_length=150)
    nome = models.CharField("Nome Completo:", max_length=164)
    # senha = models.CharField("Senha: ",max_length=50,)

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Banco de Curriculo"

    def __str__(self):
        return f'{self.nome} - {self.cpf}'

    def get_absolute_url(self):
        return reverse("Candidato_detail", kwargs={"pk": self.id})