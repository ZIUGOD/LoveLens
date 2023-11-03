from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.db import models
from .models import Image


class ImageCreateView(CreateView):
    model = Image
    fields = ["title", "image"]
    template_name = "components/create_image.html"

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para a página inicial após o upload.
        return reverse("home_page")


class ImageListView(ListView):
    model = Image
    template_name = "gallery/index.html"


class ImageDetailView(DetailView):
    model = Image
    template_name = "gallery/image_detail.html"
    context_object_name = "image"


class ImageDeleteView(DeleteView):
    model = Image
    template_name = "gallery/image_delete.html"
    success_url = reverse_lazy(
        "home_page"
    )  # Redireciona para a página inicial após a exclusão
    context_object_name = "image"
