from django.urls import path, include
from . import views as myapp_views

urlpatterns = [
    path('', myapp_views.home,name='home')
]
