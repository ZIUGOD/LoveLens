from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import ImageListView

# URLs do aplicativo
urlpatterns = [
    path("", ImageListView.as_view(), name="home_page"),
    path("image/", include("gallery.urls")),  # rota genérica
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# a linha acima adiciona as configurações para servir arquivos de mídia em desenvolvimento
