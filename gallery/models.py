# Importa o módulo de modelos do Django
from django.db import models


# Definindo o modelo `Image`:
class Image(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Retorna o título da imagem como uma representação legível


# O modelo 'Image' representa uma imagem com um título, a imagem em si e a data de upload.
