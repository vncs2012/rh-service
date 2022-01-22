from jet.admin import CompactInline
from django.contrib import admin
from .models import Vagas, Questionario, Cargos, Departamento, Perguntas
from .util import gerarImagem
# Register your models here.


class PerguntasInline(CompactInline):
    model = Perguntas
    extra = 1
    show_change_link = True


class QuestionarioAdmin(admin.ModelAdmin):
    inlines = (PerguntasInline,)


@admin.action(description='Gerar Imagem de divugação')
def imageDivugacao(modeladmin, request, queryset):
    gerarImagem(queryset)
    return 1
class VagasAdmin(admin.ModelAdmin):
    actions = [imageDivugacao]

admin.site.register(Departamento)
admin.site.register(Cargos)
admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Perguntas)
admin.site.register(Vagas,VagasAdmin)
