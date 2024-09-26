from django.urls import path
from cart_app.views import (
    CartView,
    CartAddView,
    CartSetView,
    CartDeleteView,
    CartClearView,
    CartSendView,
)

app_name = "cart_app"

urlpatterns = [
    path("", CartView.as_view(), name="list"),
    path("add/", CartAddView.as_view(), name="add"),
    path("set/", CartSetView.as_view(), name="set"),
    path("delete/", CartDeleteView.as_view(), name="delete"),
    path("clear/", CartClearView.as_view(), name="clear"),
    path("send/", CartSendView.as_view(), name="send"),
]
