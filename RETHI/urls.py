from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('participante/', include('participantes.urls')),
    path('empresa/', include('empresa.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    path('jet/', include(('jet.urls', 'jet'))),  # Django JET URLS
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
