# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

TIPO_QUESTIONARIO = ((None, ''), (1, 'PERFECCIONISTA'), (2, 'PRESTATIVO'), (3, 'BEM-SUCEDIDO'), (4, 'ROMÂNTICO'),
                     (5, "OBSERVADOR"), (6, 'QUESTIONADOR'), (7, 'SONHADOR'), (8, 'CONFRONTADOR'), (9, 'PRESERVACIONISTA'),)

TIPO_CRC = ((None, ''), (1, 'PADRÃO'), (2, 'PREDOMINANTE'),)

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.email}'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)

class EneaTipo(models.Model):
    cd_enae_tipo = models.AutoField(primary_key=True, editable=False)
    no_enae_tipo = models.CharField("Enae tipo", max_length=50, blank=False)
    nu_enae_tipo = models.CharField( "Nº do Enae Tipo", max_length=1, blank=False)

    def __str__(self):
        return self.no_enae_tipo

class PerguntaQuestionario(models.Model):

    cd_per_questionario = models.AutoField(primary_key=True, editable=False)
    nu_pergunta = models.CharField("Nº Pergunta", max_length=2, blank=False)
    ds_pergunta = models.CharField("Pergunta", max_length=250, blank=False)
    res_per_questionarioA = models.CharField("Alternativa (A)", max_length=100, blank=False)
    val_per_questionarioA = models.IntegerField('Tipo Resposta A', choices=TIPO_QUESTIONARIO )
    res_per_questionarioB = models.CharField("Alternativa (B)", max_length=100, blank=False)
    val_per_questionarioB = models.IntegerField('Tipo Resposta b', choices=TIPO_QUESTIONARIO)

    def __str__(self):
        return self.nu_pergunta

class CaracteristicasPersona(models.Model):
    cd_caracteristica = models.AutoField(primary_key=True, editable=False)
    no_caracteristica = models.CharField("Caracteristica ", max_length=100, blank=False)
    tp_caracteristica = models.IntegerField('Tipo ', choices=TIPO_QUESTIONARIO )
    tp_predominate    = models.IntegerField('Predominante? ', choices=TIPO_CRC )
    
    def __str__(self):
        return self.no_caracteristica

class Participantes(models.Model):
    cd_participante = models.AutoField(primary_key=True, editable=False)
    no_participante = models.CharField('Nome ', max_length=130,blank=True)
    nu_cpf = models.CharField('CPF ', max_length=11, null=True,blank=True)
    Tel_numero = models.CharField('Telefone ', max_length=14,blank=True)

    def __str__(self):
        return f'{self.no_participante} - {self.nu_cpf}'
    