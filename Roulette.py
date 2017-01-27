# Import libraries called intertools and random
import itertools
import random

# Fix a seed, say 3456, so that even random draws can be replicated
random.seed(3456)

# Test whether the seed works correctly: expected random outcome: 7, 8, 5, 3, 9
five_random_integers = [random.randint(1, 10) for _ in itertools.repeat(None, 5)]
print(five_random_integers)
print("The seed works as expected")


# Create a roulette game

class Table(object):  # Start with Table as a class, Roulette is going to be a subclass
    def __init__(self, min_amount=0):  # add customers=None
        self.min_amount = min_amount
#        self.customers = customers

    def above_minimum(self, betted_amounts):  # The function takes a list of betted amounts and returns a list of booleans
        valid_bets = [amount >= self.min_amount for amount in betted_amounts]
        return valid_bets

#    bet_range = range(0)  # Range of numbers on which a bet can be placed
#    bet_on = [random.randint(self.bet_range[0], self.bet_range[1]) for _ in self.customers]  # randomly chooses bets


class Roulette(Table):
#    bet_range = range(0, 36)

#    def minimum_amount(self):  # The function determines the minimum amount to be betted in a roulette game
#        self.min_amount = random.choice([50, 100, 200])

    def spin_the_wheel(self, bets):  # The function tells which players won (ignoring the minimum amount to be betted)
        draw = random.randint(0, 36)
        winning_bets = [bet == draw for bet in bets]
        print("Spinning the wheel...")
        print("the ball lands on %s." % str(draw))
        print("There are %s correct bets." % str(sum(winning_bets)))
        if any(winning_bets):
            players = [i for i in enumerate(winning_bets)]
            print("Players number %s won." % str([x[0]+1 for x in players if x[1]]))
        else:
            print("No player won.")
        return winning_bets

    def simulate_game(self, bets, betted_amounts):  # The function returns the total amount won by the casino and a list with the amounts won by the players (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.spin_the_wheel(bets)
        prize_factor = 30
        award = [valid * winning * amount * prize_factor for valid, winning, amount in zip(valid_bets, winning_bets, betted_amounts)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]


# Create a craps game

class Craps(Table):
#    bet_range = range(2, 12)

#    def set_minimum(self):
#        """Randomly sets the minimum bet"""
#       self.min_amount = random.choice([0, 25, 50])

    def dices(self, n=2):  # The function rolls 2 dices and gives their sum
        sum_dices = 0
        for i in range(n):
            sum_dices += random.randint(1, 6)
        return sum_dices

    def roll_the_dices(self, bets): # The function tells which players won (ignoring minimum bet)
        draw = self.dices()
        winning_bets = [bet == draw for bet in bets]
        print("Rolling the dices...")
        print("the dices sum to %s." % str(draw))
        if any(winning_bets):
            players = [i for i in enumerate(winning_bets)]
            print("Players number %s won." % str([x[0] + 1 for x in players if x[1]]))
        else:
            print("No player won.")
        return winning_bets

    def simulate_game(self, bets, betted_amounts): # The function returns the total amount won by the casino and a list with the amounts won by the players (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.roll_the_dices(bets)
        prize_factor = 30
        award = [valid * winning * amount * prize_factor for valid, winning, amount in zip(valid_bets, winning_bets, betted_amounts)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]




