from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PerguntaQuestionario, CaracteristicasPersona, RelatorioProfile


class PerguntaQuestionarioAdmin(admin.ModelAdmin):
    fields = ['nu_pergunta', 'ds_pergunta', 'res_per_questionarioA',
              'val_per_questionarioA', 'res_per_questionarioB', 'val_per_questionarioB']
    list_display = ('nu_pergunta', 'ds_pergunta')
    search_fields = ('nu_pergunta', 'ds_pergunta')
    ordering = ('nu_pergunta',)


class CaracteristicasPersonaAdmin(admin.ModelAdmin):
    list_display = ('no_caracteristica',
                    'tp_caracteristica', 'tp_predominate',)
    list_display_links = ('no_caracteristica',)
    search_fields = ('no_caracteristica',)
    list_filter = ('tp_predominate', 'tp_caracteristica')
    list_editable = ('tp_predominate', 'tp_caracteristica')
    list_per_page = 15


class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('email', 'participante',)
    list_display_links = ('email',)
    search_fields = ('email', 'participante')
    list_per_page = 15


admin.site.register(CaracteristicasPersona, CaracteristicasPersonaAdmin)
admin.site.register(PerguntaQuestionario, PerguntaQuestionarioAdmin)
