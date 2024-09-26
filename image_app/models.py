from django.db import models
from server.base import Directory


class Image(Directory):
    image = models.ImageField(
        verbose_name="Файл изображения",
        upload_to='images/',
        blank=True,
        null=True,
        default=""
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
