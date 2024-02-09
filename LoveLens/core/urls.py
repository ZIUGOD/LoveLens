from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import ImageListView

urlpatterns = [
    path("", ImageListView.as_view(), name="home_page"),
    path("image/", include("gallery.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
