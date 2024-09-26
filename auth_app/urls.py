from django.urls import path
from auth_app.views import TokenView

app_name = "auth_app"

urlpatterns = [
    path("get-token/", TokenView.as_view(), name="get-token"),
]
