from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    title = models.CharField(
        max_length=128,
        help_text="Max 128 characters. Required.",
        verbose_name="Image title",
    )
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="LoveLens/images/",
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(
        blank=True,
        null=True,
        max_length=1024,
        help_text="Enter the image description. Max 1024 characters. Optional.",
        verbose_name="Description",
    )

    def __str__(self):
        return self.title
