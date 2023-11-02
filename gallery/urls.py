from django.urls import path
from .views import (
    ImageCreateView,
    ImageDeleteView,
    ImageDetailView,
)

app_name = "gallery"

urlpatterns = [
    path("upload/", ImageCreateView.as_view(), name="create_image"),
    path("<int:pk>/", ImageDetailView.as_view(), name="detail_image"),
    path("<int:pk>/delete/", ImageDeleteView.as_view(), name="delete_image"),
]
