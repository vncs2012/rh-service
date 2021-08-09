from django.db import models
from empresa.models import Empresa

# Create your models here.

class Participantes(models.Model):
    cd_participante = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField('E-mail', max_length=254)
    participante = models.CharField('Nome do participante', max_length=130, blank=True)
    foto = models.ImageField(upload_to='participantes/%d/%m/%Y/', blank=True, null=True)
    empresa = models.ForeignKey(Empresa, verbose_name="Empresa Relacionada", on_delete=models.CASCADE,blank=True, null=True)
    questionario = models.BooleanField("Respondeu?" ,default=False ,blank=True, null=True)

    def __str__(self):
        return f'{self.email}'