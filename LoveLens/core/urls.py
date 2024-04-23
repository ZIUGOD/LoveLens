from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from gallery.views import ImageListView
from django.conf.urls.static import static

urlpatterns = [
    path("", ImageListView.as_view(), name="home_page"),
    path("image/", include("gallery.urls")),
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
