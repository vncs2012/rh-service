from django.urls import path, include
from Core import views as myapp_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', myapp_views.index, name='index', ),
    path('login',  myapp_views.login , name='login'),
    path('logout', myapp_views.logout, name='logout'),
    path('questionario', myapp_views.questionario, name='questionario'),
    path('usuario/add', myapp_views.create_user, name='create_user'),
]
