from typing import Union
from pydantic import BaseModel


class CartSummary(BaseModel):
    total_items: int
    subtotal: float
    tax: Union[str, float]
    shipping: float
    total_balance_due: float


class ItemRow(BaseModel):
    sku: str
    product: str
    unit_price: float
    quantity: int
    total: float
