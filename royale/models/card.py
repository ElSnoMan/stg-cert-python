from pydantic.dataclasses import dataclass


@dataclass
class Card:
    id: int
    cost: int
    icon: str
    name: str
    type: str
    arena: int
    rarity: str
