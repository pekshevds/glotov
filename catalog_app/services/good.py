from typing import List
from django.db.models import Q
from django.db import transaction
from catalog_app.models import Good, Manufacturer, Category
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.category import handle_category


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_image_list(image_list: List[dict], good: Good):
    pass


def handle_good(good_dir: dict) -> Good:
    good_id = good_dir.get("id", None)
    good = Good.objects.get_or_create(id=good_id)
    good.name = good_dir.get("name", good.name)
    good.code = good_dir.get("code", good.code)
    good.description = good_dir.get("description", good.description)
    good.balance = good_dir.get("balance", good.balance)
    good.art = good_dir.get("art", good.art)
    good.comment = good_dir.get("comment", good.comment)

    key_name = "manufacturer"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.manufacturer = None if temp_dir is None else handle_manufacturer(temp_dir)

    key_name = "cartegory"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.category = None if temp_dir is None else handle_category(temp_dir)
    good.save()
    return good


def handle_good_list(good_list: dict) -> List[Good]:
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)
            key_name = "images"
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                handle_image_list(temp_dir, good)

            goods_id.append(good.id)

    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(search: str):
    queryset = Good.objects.filter(Q(name__icontains=search) | Q(art__icontains=search))
    return queryset


def fetch_goods_queryset_by_manufacturer(manufacturers: List[Manufacturer]):
    queryset = Good.objects.filter(manufacturer__in=manufacturers)
    return queryset


def fetch_goods_queryset_by_category(categories: List[Category]):
    queryset = Good.objects.filter(manufacturer__in=categories)
    return queryset


def fetch_goods_queryset_by_group(group: Good):
    queryset = Good.objects.filter(parent=group).order_by("-is_group", "name")
    return queryset


def fetch_goods_queryset_by_filters(
    manufacturers: List[Manufacturer], categories: List[Category]
):
    filters = Q()
    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), Q.AND)

    if categories:
        filters.add(Q(category__in=categories), Q.AND)

    queryset = Good.objects.filter(filters)
    return queryset
