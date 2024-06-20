from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import ImageForm
from .models import Image


class ImageCreateView(CreateView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Image
    template_name = "gallery/create_image.html"
    success_url = reverse_lazy("home_page")
    form_class = ImageForm

    def get_queryset(self):
        return Image.objects.filter(author=self.request.user)


class ImageListView(ListView):
    model = Image
    paginate_by = None
    context_object_name = "images"
    template_name = "gallery/index.html"


class ImageDetailView(DetailView):
    model = Image
    template_name = "gallery/detail_image.html"
    context_object_name = "image"


class ImageDeleteView(DeleteView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Image
    template_name = "gallery/image_delete.html"
    success_url = reverse_lazy("home_page")
    context_object_name = "image"

    def get_queryset(self):
        return Image.objects.filter(author=self.request.user)