import json
from typing import Any
from rest_framework.test import APITestCase
from random import choices
from string import printable
from rest_framework.authtoken.models import Token
from auth_app.models import User
from catalog_app.models import Good
from django.core.serializers.json import DjangoJSONEncoder


def generating_category_name():
    return choices(printable)


def object_to_dict(object: Any, fields: list[str]) -> dict[str, Any]:
    return {field: getattr(object, field) for field in fields}


class CategoryTestCase(APITestCase):
    def setUp(self) -> None:
        self._user = User.objects.create(username="test", email="test@mail.ru")
        self._token = Token.objects.create(user=self._user)
        self._good = Good.objects.create(name="good1")

    def test__upload_goods__(self) -> None:
        data = {
            "data": [
                object_to_dict(self._good, ["id", "name"]),
            ]
        }
        url = "/api/v1/catalog/upload/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self._token.key)
        response = self.client.post(
            url,
            json.dumps(data, cls=DjangoJSONEncoder),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)


# https://docs.djangoproject.com/en/4.2/topics/testing/overview/
