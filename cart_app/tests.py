from decimal import Decimal
from django.test import TestCase
from catalog_app.models import Good
from auth_app.models import Token


class CartTest(TestCase):
    def setUp(self):
        self._good1 = Good.objects.create(name="good1")
        self._good2 = Good.objects.create(name="good2")
        self._good3 = Good.objects.create(name="good3")
        self._token1 = Token.objects.create()

    def test_cart(self):
        response = self.client.get(f"/api/v1/cart/?token={str(self._token1)}")
        self.assertEqual(response.status_code, 200)

    def test_add_cart(self):
        resp = self.client.get(
            f"/api/v1/cart/add/?token={str(self._token1)}&id={self._good1.id}"
        )
        self.assertEqual(resp.status_code, 200)

        cart = resp.data
        self.assertIsNotNone(cart, None)
        self.assertEqual(len(cart.get("data")), 1)

        resp = self.client.get(
            f"/api/v1/cart/add/?token={str(self._token1)}&id={self._good2.id}"
        )

        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(
            f"/api/v1/cart/add/?token={str(self._token1)}&id={self._good3.id}"
        )
        self.assertEqual(resp.status_code, 200)

    def test_set_cart(self):
        resp = self.client.get(
            f"/api/v1/cart/set/?token={str(self._token1)}&id={self._good1.id}&qnt=5"
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(
            f"/api/v1/cart/set/?token={str(self._token1)}&id={self._good2.id}"
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(
            f"/api/v1/cart/set/?token={str(self._token1)}&id={self._good3.id}&qnt=5"
        )
        self.assertEqual(resp.status_code, 200)
        cart = resp.data
        self.assertIsNotNone(cart, None)
        cart_items = cart.get("data")
        self.assertEqual(len(cart_items), 3)
        item3 = cart_items[2]
        self.assertEqual(Decimal(item3.get("qnt")), Decimal("5"))
        self.assertNotEqual(Decimal(item3.get("qnt")), Decimal("1"))

    def test_delete_cart(self):
        resp = self.client.get(
            f"/api/v1/cart/delete/?token={str(self._token1)}&id={self._good1.id}&qnt=5"
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(
            f"/api/v1/cart/delete/?token={str(self._token1)}&id={self._good2.id}&qnt=5"
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(
            f"/api/v1/cart/delete/?token={str(self._token1)}&id={self._good3.id}&qnt=5"
        )
        self.assertEqual(resp.status_code, 200)

    def test_clear_cart(self):
        resp = self.client.get(f"/api/v1/cart/clear/?token={str(self._token1)}")
        self.assertEqual(resp.status_code, 200)
        cart = resp.data
        self.assertEqual(len(cart.get("data")), 0)
