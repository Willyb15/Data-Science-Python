import random

class DiceRoller:

    def __init__(self, n_dice=9, n_sides=6, strategy=sum):
        self.n_dice = n_dice
        self.n_sides = n_sides
        self.strategy = strategy

    def roll(self):
        rolls = [random.randint(1, self.n_sides + 1)
                 for _ in range(self.n_dice)]
        return self.strategy(rolls)
