from django.contrib import admin

from .models import Empresa,SolicitacaoReltorio,EmpresaUsuarios
from .forms import EmpresaForm,SolicitacaoReltorioForm

# Register your models here.
class EmpresaUsuariosInline(admin.TabularInline):
    model = EmpresaUsuarios
    extra = 1
    show_change_link = True
   
    def get_queryset(self, request):
        """Alter the queryset to return no existing entries"""
        # get the existing query set, then empty it.
        qs = super(EmpresaUsuariosInline, self).get_queryset(request)
        return qs.all()

class EmpresaAdmin(admin.ModelAdmin):
    inlines= (EmpresaUsuariosInline,)
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
