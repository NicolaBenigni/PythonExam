# Import libraries called intertools and random
import itertools
import random

# Fix a seed, say 3456, so that even random draws can be replicated
random.seed(3456)

# Test whether the seed works correctly: expected random outcome: 7, 8, 5, 3, 9
five_random_integers = [random.randint(1, 10) for _ in itertools.repeat(None, 5)]
print(five_random_integers)


# Create a roulette game

class Table(object):
    def above_min(self, amount):
        return self

    def spin_the_wheel(self, bet):
        return self

    def simulate_game(self, bet, amount):
        return self


class Roulette(Table):
    def __init__(self, min_bet):
        self.min_bet = min_bet

    def above_min(self, amount):
        if amount >= self.min_bet:
            return 1
        else:
            return 0

    def spin_the_wheel(self, bet):
        print("spinning the wheel...")
        print("the ball lands on %s." % random.randint(0, 36))
        if bet == random.randint(0, 36):
            return "the bet is correct"
        else:
            return "the bet is incorrect"

    def simulate_game(self, bet, amount):
        if bet == random.randint(0, 36) and self.above_min == 1:
            return [0, amount*30]
        else:
            return [amount, 0]




