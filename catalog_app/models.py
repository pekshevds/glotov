from django.db import models
from server.base import Base
from server.base import Directory
from image_app.models import Image


class Good(Directory):
    art = models.CharField(
        verbose_name="Артикул",
        max_length=50,
        blank=True,
        null=False,
        default="",
        db_index=True,
    )
    code = models.CharField(
        verbose_name="Код", max_length=11, blank=True, null=False, default=""
    )
    balance = models.DecimalField(
        verbose_name="Остаток",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        verbose_name="Изображение (превью)",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(verbose_name="Активен", default=False)
    manufacturer = models.CharField(
        verbose_name="Производитель", max_length=100, blank=True, null=False, default=""
    )
    description = models.CharField(
        verbose_name="Описание", max_length=1024, blank=True, null=False, default=""
    )

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class GoodsImage(Base):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="images",
    )
    image = models.ForeignKey(
        Image, on_delete=models.PROTECT, verbose_name="Изображение"
    )

    def __str__(self) -> str:
        return self.image.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения товара"
