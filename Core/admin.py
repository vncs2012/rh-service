from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile, PerguntaQuestionario
from Core.models import CaracteristicasPersona, EneaTipo, Participantes


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# @admin.register(User)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    inlines = (UserProfileInline, )


# @admin.register(PerguntaQuestionario)
class PerguntaQuestionarioAdmin(admin.ModelAdmin):
    fields = ['nu_pergunta', 'ds_pergunta', 'res_per_questionarioA',
              'val_per_questionarioA', 'res_per_questionarioB', 'val_per_questionarioB']
    list_display = ('nu_pergunta', 'ds_pergunta')
    search_fields = ('nu_pergunta', 'ds_pergunta')
    ordering = ('nu_pergunta',)

class CaracteristicasPersonaAdmin(admin.ModelAdmin):
    list_display = ('no_caracteristica','tp_caracteristica','tp_predominate',)
    list_display_links = ('no_caracteristica',)
    search_fields = ('no_caracteristica',)
    list_filter = ('tp_predominate', 'tp_caracteristica')
    list_editable = ('tp_predominate','tp_caracteristica')
    list_per_page = 15

class EneaTipoaAdmin(admin.ModelAdmin):
    list_display = ('no_enae_tipo','nu_enae_tipo')
    search_fields = ('no_enae_tipo',)
    list_per_page = 15

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('nu_cpf','no_participante','Tel_numero',)
    list_display_links = ('nu_cpf',)
    search_fields = ('nu_cpf','no_participante')
    list_per_page = 15

admin.site.register(CaracteristicasPersona,CaracteristicasPersonaAdmin)
admin.site.register(EneaTipo,EneaTipoaAdmin)
admin.site.register(Participantes,ParticipantesAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(PerguntaQuestionario, PerguntaQuestionarioAdmin)
