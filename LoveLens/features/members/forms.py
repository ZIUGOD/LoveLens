"""
This module contains the form classes for user registration.

The UserRegisterForm class is a subclass of Django's UserCreationForm
and adds an email field to the form.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user.
    """

    email = forms.EmailField()

    class Meta:
        """
        Meta class for the UserRegisterForm.
        """

        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]
