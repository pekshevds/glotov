from django.test import TestCase


class AuthTest(TestCase):
    def setUp(self):
        pass

    def test_cart(self):
        resp = self.client.get("/api/v1/auth/get-token/")
        self.assertEqual(resp.status_code, 200)
