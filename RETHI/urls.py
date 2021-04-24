from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('empresa/', include('empresa.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    path('jet/', include(('jet.urls', 'jet'))),  # Django JET URLS
]
