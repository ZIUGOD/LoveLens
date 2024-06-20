"""
This module contains the Image model for the LoveLens application.
The Image model represents an image uploaded by a user.
It contains the image file, a title, a description,
and the user who uploaded it.
"""

from django_currentuser.db.models import CurrentUserField
from django.dispatch import receiver
from django.db.models.signals import post_delete
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone


class Image(models.Model):
    """
    This model represents an image uploaded by a user.
    It contains the image file, a title, a description, and the user who uploaded it.
    """

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
    )
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="LoveLens/sent_images/",
    )
    description = RichTextField(
        verbose_name="Description",
        max_length=128,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at: ",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at: ",
    )
    author = CurrentUserField(
        related_name="user_pictures",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)[:128]


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    # Pass False so FileField doesn't save the model.
    if instance.image:
        instance.image.delete(False)
