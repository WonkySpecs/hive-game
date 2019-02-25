from enum import Enum, auto
from dataclasses import dataclass


class Creature(Enum):
    QUEEN = auto()
    BEETLE = auto()
    GRASSHOPPER = auto()
    SPIDER = auto()
    ANT = auto()


@dataclass(frozen=True)
class Tile:
    __slots__ = 'creature', 'player'
    creature: Creature
    player: int

    def __str__(self):
        return f"Player {self.player} {self.creature}"
