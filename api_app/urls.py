from django.urls import path, include


app_name = "api_app"

urlpatterns = [
    path("catalog/", include("catalog_app.urls", namespace="catalog_app")),
    path("cart/", include("cart_app.urls", namespace="cart_app")),
    path("auth/", include("auth_app.urls", namespace="auth_app")),
]
