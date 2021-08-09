from django.contrib import admin
from .models import Candidato, DadosEscolaridade, DadosPessoas, DadosProfissionais, QuestionarioPadrao,vagasCandidato
from jet.admin import CompactInline


class DadosPessoasInline(admin.TabularInline):
    model = DadosPessoas
    extra = 1
    show_change_link = True


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
    extra = 1
    show_change_link = True

class candidatoInline(admin.TabularInline):
    model = Candidato
    extra = 1
    show_change_link = True



class CandidatoAdmin(admin.ModelAdmin):
    inlines = (DadosPessoasInline, DadosEscolaridadeInline,
               DadosProfissionaisInline, QuestionarioPadraoInline,vagasCandidatoInline)
    # form = EmpresaForm
    list_display = ('nome', 'email',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 15


admin.site.register(Candidato, CandidatoAdmin)
