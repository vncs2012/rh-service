from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .utils import TIPO_RELATORIO

class Empresa(models.Model):
    """Pode sera tanto Empresa Consultor ou coach"""
    user_admin = models.OneToOneField(User, verbose_name="Usuario Administrador", on_delete=models.CASCADE)
    nome = models.CharField("Empresa  & Consultor", max_length=128)
    email = models.EmailField("E-mail", max_length=128)
    contato = models.CharField("Telefone de Contato", max_length=12)
    status = models.BooleanField("Status", default=True)
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresa & Consultor"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Empresa_detail", kwargs={"pk": self.id})

class EmpresaUsuarios(models.Model):
    id_empresa = models.ForeignKey(Empresa, verbose_name="Empresa", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "EmpresaUsuarios"
        verbose_name_plural = "Empresa & Usuarios"

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Empresa_detail", kwargs={"pk": self.id})

class SolicitacaoReltorio(models.Model):
    empresa = models.ForeignKey(Empresa, verbose_name=("Empresa  & Consultor"), on_delete=models.CASCADE)
    quantidade_solicitada = models.IntegerField("Quantidade",)
    preco = models.DecimalField("Valor da Solicitação", max_digits=10, decimal_places=2,null=True,blank=True)
    quantidade_restante = models.IntegerField("Quantidade Restante de Relatorio",blank=True,null=True)
    status =  models.BooleanField("Status Solicitação",default=False,editable=False)
    tipo_relatorio =  models.CharField(max_length=4,choices=TIPO_RELATORIO, default=None)
    data_solicitacao = models.DateField("Data Solicitação", auto_now=True, auto_now_add=False, blank=True, null=True)
    
    class Meta:
        verbose_name = "SolicitacaoReltorio"
        verbose_name_plural = "Solicitacão de Relatórios"

    def __str__(self):
        return f'Solicitação de {self.quantidade_solicitada} foi realizada ' 

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.id})

