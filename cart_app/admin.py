from django.contrib import admin
from cart_app.models import Recipient, CartItem


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "token",
        "good",
        "qnt",
    )
