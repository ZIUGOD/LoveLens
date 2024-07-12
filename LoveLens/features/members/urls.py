"""
This module contains the URL patterns for the members app.

It includes the following URL patterns:
- login_user: URL for member login.
- user_profile: URL for user profile page.
"""

from django.urls import path
from .views import MemberLoginView, UserProfileView, UserRegisterView



urlpatterns = [
    path("login/", MemberLoginView.as_view(), name="login_user"),
    path("u/<str:username>/", UserProfileView.as_view(), name="user_profile"),
    path("sign-up/", UserRegisterView.as_view(), name="register_user"),
]
