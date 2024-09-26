import hashlib
from django.http import HttpRequest
from django.db.models import Q
from django.db.models import QuerySet
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.category import category_by_id_list
from catalog_app.models import Good


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode("utf-8"))
    return hash.hexdigest()


def fetch_filters(request: HttpRequest) -> list[QuerySet]:
    manufacturers = None
    obj_id = request.GET.get("manufacturer_id")
    if obj_id:
        manufacturers = manufacturer_by_id_list(obj_id.split(","))

    categories = None
    obj_id = request.GET.get("category_id")
    if obj_id:
        categories = category_by_id_list(obj_id.split(","))
    return [categories, manufacturers]


def fetch_goods_by_filters(args) -> QuerySet:
    queryset = fetch_goods_queryset_by_filters(args[0], args[1])
    return queryset


def fetch_goods_queryset_by_filters(
    categories: list[object], manufacturers: list[object]
) -> QuerySet | None:
    filters = Q()
    condition = Q.AND
    if categories:
        filters.add(Q(category__in=categories), condition)

    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), condition)

    if len(filters) > 0:
        return Good.objects.filter(filters)
    return None
