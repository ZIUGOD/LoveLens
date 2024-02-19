from crispy_forms.helper import FormHelper
from .models import Image
from ckeditor.widgets import CKEditorWidget  # Add missing import statement
from django import forms


class ImageForm(forms.ModelForm):
    """
    A form for creating or updating an Image object.

    This form is used to handle the creation and updating of Image objects.
    It includes fields for the title and text of the image.

    Attributes:
        title (CharField): The title of the image.
        text (CharField): The text of the image.
    """

    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Image
        fields = ["title", "image", "description"]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_tag = False
        self.helper.label_class = "col-lg-2"
