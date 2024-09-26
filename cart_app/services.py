from typing import Sequence, TypeAlias
from decimal import Decimal
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.template import loader
from auth_app.models import Token
from cart_app.models import Recipient, CartItem
from catalog_app.models import Good

CartItems: TypeAlias = QuerySet[CartItem]


def get_token(token: str) -> Token:
    return get_object_or_404(Token, id=token)


def get_good(good_id: str) -> Good:
    return get_object_or_404(Good, id=good_id)


def get_cart(token: Token) -> CartItems:
    return CartItem.objects.filter(token=token).all()


def add_to_cart(token: Token, good: Good, qnt: Decimal = Decimal("1")) -> None:
    cart_item, _ = CartItem.objects.get_or_create(token=token, good=good)
    cart_item.qnt += qnt
    cart_item.save()


def set_to_cart(token: Token, good: Good, qnt: Decimal = Decimal("1")) -> None:
    cart_item, _ = CartItem.objects.get_or_create(token=token, good=good)
    cart_item.qnt = qnt
    cart_item.save()


def delete_from_cart(token: Token, good: Good, qnt: Decimal = Decimal("1")) -> None:
    cart_item = CartItem.objects.filter(token=token, good=good).first()
    if cart_item:
        if cart_item.qnt <= qnt:
            cart_item.delete()
        else:
            cart_item.qnt -= qnt
            cart_item.save()


def clear_cart(token: Token) -> None:
    CartItem.objects.filter(token=token).delete()


def prepare_html_message(context: dict):
    return loader.render_to_string("cart_app/message.html", context)


def send_cart(context: dict) -> bool:
    recipient_list = [recipient.email for recipient in Recipient.objects.all()]
    result = 0
    if len(recipient_list) > 0:
        html_message = prepare_html_message(context)
        result = send_mail(
            "Корзина",
            "Сообщение",
            None,
            recipient_list=recipient_list,
            html_message=html_message,
        )
    return True if result == 1 else False


__all__: Sequence[str] = (
    "get_cart",
    "add_to_cart",
    "delete_from_cart",
    "clear_cart",
    "set_to_cart",
    "send_cart",
)
