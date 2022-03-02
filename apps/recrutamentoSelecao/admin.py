from jet.admin import CompactInline
from django.contrib import admin
from .models import Vagas, Questionario, Cargos, Departamento, Perguntas, Entrevista
from .util import gerarImagem
# Register your models here.


class PerguntasInline(CompactInline):
    model = Perguntas
    extra = 1
    show_change_link = True


class QuestionarioAdmin(admin.ModelAdmin):
    inlines = (PerguntasInline,)


class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'departamento', 'status')
    list_display_links = ('nome',)
    search_fields = ('nome', 'departamento', 'status')
    list_filter = ('departamento', 'status')
    list_editable = ('status',)
    list_per_page = 15


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 15


class PerguntasAdmin(admin.ModelAdmin):
    list_display = ('questionario_id', 'descricao')
    list_display_links = ('questionario_id',)
    search_fields = ('descricao',)
    list_filter = ('questionario_id',)
    list_per_page = 15


@admin.action(description='Gerar Imagem de divugação')
def imageDivugacao(modeladmin, request, queryset):
    return gerarImagem(request, queryset)


class VagasAdmin(admin.ModelAdmin):
    actions = [imageDivugacao]
    list_display = ('descricao', 'cargo', 'status')
    list_display_links = ('descricao',)
    search_fields = ('descricao', 'cargo', 'status')
    list_filter = ('cargo', 'status')
    list_editable = ('status',)
    list_per_page = 15


class EntrevistaAdmin(admin.ModelAdmin):
    list_display = ('id_candidato', 'status')
    list_display_links = ('id_candidato',)
    search_fields = ('id_candidato', 'status')
    list_filter = ('id_candidato', 'status')
    list_editable = ('status',)
    list_per_page = 15


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Cargos, CargoAdmin)
admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Perguntas, PerguntasAdmin)
admin.site.register(Vagas, VagasAdmin)
admin.site.register(Entrevista, EntrevistaAdmin)
