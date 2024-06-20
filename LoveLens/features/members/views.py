"""
This module contains views related to member functionality.

It includes views for member login and user profile display.
"""

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


class MemberLoginView(LoginView):
    """
    Login view for members. Overrides the default login view to use a custom template.
    Redirects to the home page if the user is already authenticated.
    """

    template_name = "members/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
    authentication_form = AuthenticationForm


class UserProfileView(generic.TemplateView):
    """
    This view is used to display the user's profile information.
    """

    template_name = "members/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lovelens_user"] = User.objects.filter(
            username=self.kwargs["username"]
        ).first()
        print(context)
        return context
