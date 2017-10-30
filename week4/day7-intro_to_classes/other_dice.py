from numpy.random import randint, poisson, binomial

class Die:
    def __init__(self, n_sides = 6):
        self.n_sides = n_sides

    def roll(self):
        return randint(1, self.n_sides + 1)

    def __repr__(self):
        return "Die({})".format(self.n_sides)

    def __str__(self):
        return "d{}".format(self.n_sides)

class BinomialDie:
    def __init__(self, n_sides = 6, p = 7/12.):
        self.n_sides = n_sides
        self.p = p

    def roll(self):
        return binomial(self.n_sides, self.p)

    def __repr__(self):
        return "Die({})".format(self.n_sides)

    def __str__(self):
        return "d{}".format(self.n_sides)

class PoissonDie:
    def __init__(self, average = 3.5):
        self.average = average

    def roll(self):
        return poisson(self.average)

    def __repr__(self):
        return "Die({})".format(self.n_sides)

    def __str__(self):
        return "d{}".format(self.n_sides)
