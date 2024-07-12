"""
This module contains the URL configuration for the LoveLens project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include  # , reverse_lazy
from features.gallery.views import ImageListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ImageListView.as_view(), name="home_page"),  # index
    path("", include("django.contrib.auth.urls")),  # django
    path("image/", include("features.gallery.urls")),  # app images
    path("members/", include("features.members.urls")),  # login, signup, profile
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
