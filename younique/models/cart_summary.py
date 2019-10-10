from typing import Union
from pydantic.dataclasses import dataclass


@dataclass()
class CartSummary(object):
    def __init__(self, total_items, subtotal, tax, shipping, total_balance_due):
        self.total_items: int = total_items
        self.subtotal: float = subtotal
        self.tax: Union[str, float] = tax
        self.shipping: float = shipping
        self.total_balance_due: float = total_balance_due
