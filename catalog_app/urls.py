from django.urls import path
from catalog_app.views import (
    GoodView,
    DataView,
    UploadGoodView,
)


app_name = "catalog_app"

urlpatterns = [
    path("good/", GoodView.as_view(), name="good"),
    path("data/", DataView.as_view(), name="data"),
    path("upload/", UploadGoodView.as_view(), name="upload"),
]
