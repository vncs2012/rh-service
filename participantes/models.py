from django.db import models

# Create your models here.

class Participantes(models.Model):
    cd_participante = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField('E-mail', max_length=254)
    participante = models.CharField('Nome ', max_length=130, blank=True)
    foto = models.ImageField(
        upload_to='participantes/%d/%m/%Y/', blank=True, null=True)
    codigo_confirmacao = models.CharField( max_length=50, default='123')
    # Empressa relacionada

    def __str__(self):
        return f'{self.email}'