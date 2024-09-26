from typing import Sequence
from pydantic import BaseModel


class Cart(BaseModel):
    cart_items: dict[str, float] = dict()


__all__: Sequence[str] = ("Cart",)
