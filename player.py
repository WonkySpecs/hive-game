from tile import Creature


class Player:
    def __init__(self):
        self.unplaced_creatures = [Creature.QUEEN,
                                   Creature.BEETLE,
                                   Creature.BEETLE,
                                   Creature.ANT,
                                   Creature.ANT,
                                   Creature.ANT,
                                   Creature.SPIDER,
                                   Creature.SPIDER,
                                   Creature.SPIDER,
                                   Creature.GRASSHOPPER,
                                   Creature.GRASSHOPPER]
