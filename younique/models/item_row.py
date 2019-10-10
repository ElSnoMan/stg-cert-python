from pydantic.dataclasses import dataclass


@dataclass()
class ItemRow(object):
    def __init__(self, sku, product, unit_price, quantity, total):
        self.sku: str = sku
        self.product: str = product
        self.unit_price: float = unit_price
        self.quantity: int = quantity
        self.total: float = total
