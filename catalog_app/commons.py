import hashlib
from django.db.models import Q
from django.db.models import QuerySet
from catalog_app.models import Good


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode("utf-8"))
    return hash.hexdigest()


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
