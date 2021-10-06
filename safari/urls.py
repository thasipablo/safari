from safari.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('acceuil.urls')),
    path('agence/', include('agence.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
