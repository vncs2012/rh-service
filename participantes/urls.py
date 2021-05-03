from django.urls import path, include
from participantes import views as myapp_views

urlpatterns = [
    path('questionario/paricipante', myapp_views.questionario_paricipante, name='questionario_paricipante'),
    path('edit', myapp_views.paricipante_edit, name='paricipante_edit'),
    path('list', myapp_views.paricipante_list, name='paricipante_list'),
    path('create', myapp_views.create_participante, name='create_participante'),
    path('save', myapp_views.save, name='save_participante'),
]
