"""
This module contains views related to member functionality.

It includes views for member login and user profile display.
"""

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login_user")
    template_name = "registration/register.html"


class MemberLoginView(LoginView):
    """
    Login view for members. Overrides the default login view to use a custom template.
    Redirects to the home page if the user is already authenticated.
    """

    template_name = "registration/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
    authentication_form = AuthenticationForm


class UserProfileView(generic.TemplateView):
    """
    This view is used to display the user's profile information.
    """

    template_name = "registration/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lovelens_user"] = User.objects.filter(
            username=self.kwargs["username"]
        ).first()
        return context
