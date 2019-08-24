from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


@dataclass
class SubCard(Card):
    character: str
