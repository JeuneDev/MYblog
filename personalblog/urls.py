from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Accès à l'interface d'administration
    path('', include('monblog.urls')),  # Inclusion des URLs de l'application Articles
    path('auth/', include('accounts.urls')),  # Inclusion des URLs de l'application Authentification
]

# Ajout des chemins pour les fichiers médias pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
