from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import index

# URLs do aplicativo
urlpatterns = [
    path("", include("gallery.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# a linha acima adiciona as configurações para servir arquivos de mídia em desenvolvimento
