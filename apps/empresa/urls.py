from django.urls import path, include
from empresa import views as myapp_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('solicitacao/list', myapp_views.solicitacaoRelatorioList, name='solicitacaolist'),
    path('solicitacao/add', myapp_views.solicitacaoRelatorioAdd, name='solicitacaoadd'),
    path('solicitacao/save', myapp_views.solicitacaoRelatorioSave, name='solicitacaosave'),
    path('solicitacao/del/<int:solicitacao_id>', myapp_views.solicitacaoRelatoriodel, name='solicitacaodel'),
]