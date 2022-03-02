from django.urls import path, include
from recrutamentoSelecao import views as myapp_views

urlpatterns = [
    path('download/', myapp_views.download,
         name='download'),
]
