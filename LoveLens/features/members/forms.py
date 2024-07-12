from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import UserProfile


class UserRegisterForm(forms.Form):
    """
    Form for registering a new user.
    """

    email = forms.EmailField()
