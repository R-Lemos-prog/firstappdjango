from django.urls import reverse
from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

    # Gera a alteração de exibição: Ex. "O video “Video: Aperitivo Motivação” foi alterado com sucesso."

    def __str__(self):
        return f'Video: {self.titulo}'
