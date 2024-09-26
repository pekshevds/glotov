from django.db.models import QuerySet
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list,
)
from catalog_app.models import Manufacturer


def manufacturer_by_id(id: str) -> Manufacturer | None:
    return object_by_id(Manufacturer, id=id)


def manufacturer_by_id_list(id: list[str]) -> QuerySet:
    return object_by_id_list(Manufacturer, ids=id)


def handle_manufacturer(item_dir: dict) -> Manufacturer | None:
    return handle_object(Manufacturer, object_dir=item_dir)


def handle_manufacturer_list(item_list: list[dict]) -> QuerySet:
    return handle_object_list(Manufacturer, object_list=item_list)
