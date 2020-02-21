from typing import Optional, List
from pydantic import BaseModel, Field
from deck_of_cards.cards import Card


class BaseResponse(BaseModel):
    error: Optional[str] = None
    success: bool


class Deck(BaseResponse):
    id: str = Field(..., alias='deck_id')
    remaining: int
    shuffled: Optional[bool] = None


# ACTION RESPONSES #

class CardDraw(Deck):
    """ Drawing cards returns a Deck object along with the list of Cards drawn. """
    cards: List[Card]


class ListAction(Deck):
    pass
