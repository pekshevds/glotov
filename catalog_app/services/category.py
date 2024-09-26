from typing import Any
from dataclasses import dataclass
from django.db.models import QuerySet
from catalog_app.models import Category
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list,
)


@dataclass
class Menu:
    category: Category
    items: list[Any] | None


def category_by_id(id: str) -> Category:
    return object_by_id(Category, id=id)


def category_by_id_list(id: list[str]) -> QuerySet:
    return object_by_id_list(Category, ids=id)


def handle_category(category_dir: dict) -> Category:
    return handle_object(Category, object_dir=category_dir)


def handle_category_list(category_list: list[dict]) -> QuerySet:
    return handle_object_list(Category, object_list=category_list)


def fetch_menu_by_category() -> list[Menu] | None:
    submenu1: list[Menu] = list()
    for subcategory1 in Category.objects.filter(parent=None).order_by("name"):
        submenu2: list[Menu] = list()
        for subcategory2 in Category.objects.filter(parent=subcategory1).order_by(
            "name"
        ):
            submenu3: list[Menu] = list()
            for subcategory3 in Category.objects.filter(parent=subcategory2).order_by(
                "name"
            ):
                submenu3.append(Menu(category=subcategory3, items=None))
            submenu2.append(Menu(category=subcategory2, items=submenu3))
        submenu1.append(Menu(category=subcategory1, items=submenu2))
    return submenu1
