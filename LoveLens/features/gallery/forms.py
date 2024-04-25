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
        image (ImageField): The image file.
        description (CharField): The description of the image.
    """

    title = forms.CharField(
        label="Título da imagem ",
    )
    image = forms.ImageField(
        label="Enviar imagem ",
    )
    description = forms.CharField(
        label="Descrição da imagem ",
        widget=CKEditorWidget(),
    )

    class Meta:
        model = Image
        fields = ["title", "image", "description"]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.field_class = "d-flex flex-column align-items-center w-100"
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control shadow rounded-5 py-2 px-3",
                "placeholder": "Insira um título...",
            }
        )
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control shadow rounded-5 p-2 w-100",
                "placeholder": "Inserir uma nova imagem...",
            }
        )
