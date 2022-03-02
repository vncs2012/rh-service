from django.contrib import admin
from .models import Candidato, DadosEscolaridade, DadosPessoas, DadosProfissionais, QuestionarioPadrao, vagasCandidato
from jet.admin import CompactInline
from django.utils.html import mark_safe
from .views import saveProximaFaseEntrevista


class DadosPessoasInline(CompactInline):
    model = DadosPessoas
    extra = 1
    show_change_link = False
    max_num = 1


class DadosEscolaridadeInline(CompactInline):
    model = DadosEscolaridade
    extra = 1
    show_change_link = True


class QuestionarioPadraoInline(CompactInline):
    model = QuestionarioPadrao
    extra = 1
    show_change_link = True


class DadosProfissionaisInline(CompactInline):
    model = DadosProfissionais
    extra = 1
    show_change_link = True


class vagasCandidatoInline(CompactInline):
    model = vagasCandidato
    extra = 3
    show_change_link = True
    max_num = 2


@admin.action(description='Classificar para Entrevisa!')
def proximaFaseEntrevista(modeladmin, request, queryset):
    return saveProximaFaseEntrevista(request,queryset)


class CandidatoAdmin(admin.ModelAdmin):
    actions = [proximaFaseEntrevista]
    inlines = (DadosPessoasInline, DadosEscolaridadeInline,
               DadosProfissionaisInline, QuestionarioPadraoInline, vagasCandidatoInline)
    list_display = ('nome', 'email', 'vaga')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('dadospessoas__sexo', 'dadospessoas__estado_civil',
                   'vagascandidato__id_vaga', 'dadosescolaridade__status')
    list_per_page = 15
    ordering = ('id',)

    def vaga(self, object):
        return mark_safe('\n'.join('<li>{}</li>'.format(str(s.id_vaga)) for s in vagasCandidato.objects.filter(id_candidato=object.id)))
    vaga.short_description = ("Vagas preferidas")


admin.site.register(Candidato, CandidatoAdmin)
