from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageForm


class ImageCreateView(CreateView, LoginRequiredMixin):
    model = Image
    template_name = "gallery/create_image.html"
    form_class = ImageForm
    success_url = reverse_lazy("home_page")


class ImageListView(ListView):
    model = Image
    paginate_by = None
    context_object_name = "images"
    template_name = "gallery/index.html"


class ImageDetailView(DetailView):
    model = Image
    template_name = "gallery/image_detail.html"
    context_object_name = "image"


class ImageDeleteView(DeleteView, LoginRequiredMixin):
    model = Image
    template_name = "gallery/image_delete.html"
    success_url = reverse_lazy("home_page")
    context_object_name = "image"

    def get_queryset(self):
        return Image.objects.filter(author=self.request.user)
