from crispy_forms.helper import FormHelper
from .models import Image
from django import forms


class ImageForm(forms.ModelForm):
    """
    A form for creating or updating an Image object.

    This form is used to handle the creation and updating of Image objects.
    It includes fields for the title, image, and description of the image.

    Attributes:
        title (CharField): The title of the image.
        image (ImageField): The image file.
        description (CharField): The description of the image.
    """

    file = forms.FileField(
        required=True,
        label="Image",
        help_text="Upload an image",
        error_messages={"required": "Please upload an image"},
    )

    class Meta:
        model = Image
        fields = ["title", "image", "description"]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_class = "form-control"
        self.helper.field_class = "mb-3"
        self.helper.label_class = "mb-1"
        self.helper.layout = (
            "title",
            "image",
            "description",
        )
