"""
This module contains the models for the members app.
The members app contains the UserProfile model.
"""

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    This model represents a user profile.
    It contains the user's biography and the user it belongs to.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
    biography = models.TextField(
        blank=True,
        null=True,
        default="Hey! I am using LoveLens!",
        max_length=256,
    )
