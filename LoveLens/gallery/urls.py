from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ImageCreateView,
    ImageDeleteView,
    ImageDetailView,
)

app_name = "gallery"

urlpatterns = [
    path("upload/", ImageCreateView.as_view(), name="new_image"),
    path("<int:pk>/", ImageDetailView.as_view(), name="detail_image"),
    path("<int:pk>/delete/", ImageDeleteView.as_view(), name="delete_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
