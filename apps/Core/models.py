# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext_lazy as _



TIPO_QUESTIONARIO = ((None, ''),
                     (1, 'PERFECCIONISTA'),
                     (2, 'PRESTATIVO'),
                     (3, 'BEM-SUCEDIDO'),
                     (4, 'ROMÂNTICO'),
                     (5, "OBSERVADOR"),
                     (6, 'QUESTIONADOR'),
                     (7, 'SONHADOR'),
                     (8, 'CONFRONTADOR'),
                     (9, 'PRESERVACIONISTA'),)

TIPO_CRC = ((None, ''), (1, 'PADRÃO'), (2, 'PREDOMINANTE'),)


class PerguntaQuestionario(models.Model):
    cd_per_questionario = models.AutoField(primary_key=True, editable=False)
    nu_pergunta = models.CharField("Nº Pergunta", max_length=2, blank=False)
    ds_pergunta = models.CharField("Pergunta", max_length=250, blank=False)
    res_per_questionarioA = models.CharField(
        "Alternativa (A)", max_length=100, blank=False)
    val_per_questionarioA = models.IntegerField(
        'Tipo Resposta A', choices=TIPO_QUESTIONARIO)
    res_per_questionarioB = models.CharField(
        "Alternativa (B)", max_length=100, blank=False)
    val_per_questionarioB = models.IntegerField(
        'Tipo Resposta b', choices=TIPO_QUESTIONARIO)

    def __str__(self):
        return self.nu_pergunta


class CaracteristicasPersona(models.Model):
    cd_caracteristica = models.AutoField(primary_key=True, editable=False)
    no_caracteristica = models.CharField(
        "Caracteristica ", max_length=100, blank=False)
    tp_caracteristica = models.IntegerField('Tipo ', choices=TIPO_QUESTIONARIO)
    tp_predominate = models.IntegerField('Predominante? ', choices=TIPO_CRC)

    def __str__(self):
        return self.no_caracteristica

class RelatorioProfile(models.Model):
    personalidade = models.TextField()
    profisional = models.TextField()
    caracteristicasPernonalidade = models.TextField()
    infancia = models.TextField()
    estadoInvolucao = models.TextField()
    Asas = models.TextField()
    tp_caracteristica = models.IntegerField('Tipo ', choices=TIPO_QUESTIONARIO)

    class Meta:
        verbose_name = _("Relatorio Profile")
        verbose_name_plural = _("Relatorio Profiles")

    def __str__(self):
        return f"Salvo com Sucesso {self.tp_caracteristica}"

    def get_absolute_url(self):
        return reverse("RelatorioProfile_detail", kwargs={"pk": self.id})
