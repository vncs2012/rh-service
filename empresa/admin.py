from django.contrib import admin

from .models import Empresa,SolicitacaoReltorio
from .forms import EmpresaForm,SolicitacaoReltorioForm
# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    form = EmpresaForm
    list_display = ('nome', 'email', 'contato','status')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_editable = ('status',)
    list_per_page = 15

class SolicitacaoReltorioaAdmin(admin.ModelAdmin):
    form = SolicitacaoReltorioForm
    list_display = ('empresa', 'quantidade_solicitada','preco', 'tipo_relatorio','quantidade_restante','data_solicitacao','status')
    list_display_links = ('empresa',)
    search_fields = ('empresa','tipo_relatorio')
    list_filter = ('tipo_relatorio', 'status')
    # list_editable = ('status',)
    list_per_page = 15

admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(SolicitacaoReltorio,SolicitacaoReltorioaAdmin)
