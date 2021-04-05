from django.urls import path, include
from Core import views as myapp_views

urlpatterns = [
    path('', myapp_views.index, name='index'),
    path('login', myapp_views.login, name='login'),
]
