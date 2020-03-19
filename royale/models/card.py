from pydantic import BaseModel


class Card(BaseModel):
    id: int
    cost: int
    icon: str
    name: str
    type: str
    arena: int
    rarity: str
