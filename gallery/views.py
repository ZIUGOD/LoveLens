from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse
from .models import Image


class ImageListView(ListView):
    model = Image
    template_name = "gallery/index.html"


class ImageCreateView(CreateView):
    model = Image
    fields = ["title", "image"]
    template_name = "components/create_image.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home_page")  # Redireciona para a página inicial após o upload.
