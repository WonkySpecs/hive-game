from enum import Enum, auto
from dataclasses import dataclass


class Creature(Enum):
    QUEEN = "Q"
    BEETLE = "B"
    GRASSHOPPER = "G"
    SPIDER = "S"
    ANT = "A"


@dataclass(frozen=True)
class Tile:
    __slots__ = 'creature', 'player'
    creature: Creature
    player: int

    def __str__(self):
        return f"Player {self.player} {self.creature}"

    def player_colour(self):
        return "w" if self.player == 0 else "b"

    def to_symbol(self):
        return str(self.player_colour()) + self.creature.value
