from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title  # Retorna o título da imagem como uma representação legível
