from django.test import TestCase
from catalog_app.models import Category
from random import choices
from string import printable


def generating_category_name():
    return choices(printable)


class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_creating_new_category(self) -> None:
        category_name = generating_category_name()
        new_category = Category.objects.create(name=category_name)
        found_category = Category.objects.get(name=category_name)
        self.assertEqual(found_category, new_category)

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/
