from django.db import models
from server.base import Directory, Base
from auth_app.models import Token
from catalog_app.models import Good


class Recipient(Directory):
    email = models.EmailField(verbose_name="Почта", unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"


class CartItem(Base):
    token = models.ForeignKey(Token, on_delete=models.CASCADE, verbose_name="Токен")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name="Товар")
    qnt = models.DecimalField(
        verbose_name="Количество",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = "Строка корзины"
        verbose_name_plural = "Корзина"
