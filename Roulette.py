# Import necessary libraries
import random

### This file contains the code for roulette and craps games, besides some tests for the random seed

# Fix a seed, say 3456, so that even random draws can be replicated
random.seed(3456)

# Test whether the seed works correctly: expected random outcome: 7, 8, 5, 3, 9
five_random_integers = [random.randint(1, 10) for i in range(5)]
print(five_random_integers)
if five_random_integers == [7, 8, 5, 3, 9]:
    print("The seed works as expected.")
else:
    print("Fix seed.")


# Create a roulette game

class Table(object):  # Start with Table as a class, Roulette is going to be a subclass. In the final stage the table is
    # characterized by the following elements: a game, a croupier and customers
    def __init__(self, min_amount=0, croupier=None, customers=None, profit=0):
        self.min_amount = min_amount
        self.customers = customers
        self.croupier = croupier
        self.profit = profit

    def above_minimum(self, betted_amounts):  # The function takes a list of betted amounts and returns a list of booleans
        valid_bets = [amount >= self.min_amount for amount in betted_amounts]
        return valid_bets

    def simulate_game(self, bets, betted_amounts):  # The function can take a list of bets and betted amounts and return
        #  the amount won by casino and costumers automatically taking into account the type of game played
        print("Simulating game...")

    def place_random_amount(self):  # The function bets random amounts for each customers. The function's element
        # place_amount is defined in the customers file and depends on the type of customer
        [x.place_amount(self.min_amount) for x in self.customers]

    bet_range = range(0)  # Just define bet_range. Its true value will be assigned in the subclasses

    def simulate_game_round(self):  # The function simulates the round of a game at a table, which include sharing the
        # profit with the croupier, collecting the remaining profit, paying out the awards to the customers
        self.place_random_amount()
        bets = [random.randint(self.bet_range[0], self.bet_range[1]) for _ in self.customers]  # The function randomly
        # chooses bets in the correct bet range for each customer taking into account the type of game played
        betted_amounts = [x.amount for x in self.customers]  # The function recovers a list of betted amounts per
        # customers. The function's element "amount" is defined in the customers file
        game_outcome = self.simulate_game(bets, betted_amounts)
        if game_outcome[0] > 0:
            self.croupier.fee += int(0.005 * game_outcome[0])  # The croupier shares the profit from the game
            self.profit += int(game_outcome[0] * 0.995)
        else:
            self.profit += game_outcome[0]  # The croupier does not share the losses, the casino has to bear them whole
        for x, y in zip(self.customers, game_outcome[1]):  # Each customer win his award
            x.budget += y
        return game_outcome[1]  # Returns list of values won by customers


class Roulette(Table):
    bet_range = range(0, 36)

    def minimum_amount(self):  # The function determines the minimum amount to be betted in a roulette game
        self.min_amount = random.choice([50, 100, 200])

    @staticmethod  # Static method is a function decorator that tells us that the method does not depend on the state
    # of the object itself and can be overridden in a subclass
    def spin_the_wheel(bets):  # The function tells which customer won (ignoring the minimum amount to be betted)
        draw = random.randint(0, 36)
        winning_bets = [bet == draw for bet in bets]
        print("Spinning the wheel...")
        print("the ball lands on %s." % str(draw))
        print("There are %s correct bets." % str(sum(winning_bets)))
        if any(winning_bets):
            customers = [i for i in enumerate(winning_bets)]
            print("Players number %s won." % str([x[0]+1 for x in customers if x[1]]))
        else:
            print("No player won.")
        return winning_bets

    def simulate_game(self, bets, betted_amounts):  # The function returns the total amount won by the casino and a
        # list with the amounts won by the customers (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.spin_the_wheel(bets)
        prize_factor = 30
        award = [valid * winning * amount * prize_factor for valid, winning, amount in zip(valid_bets, winning_bets,
                                                                                           betted_amounts)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]


# Create a craps game

class Craps(Table):
    bet_range = range(2, 12)

    def minimum_amount(self):  # The function determines the minimum amount to be betted in a craps game
        self.min_amount = random.choice([0, 25, 50])

    @staticmethod
    def dices():  # The function rolls 2 dices and gives their sum
        sum_dices = 0
        for i in range(2):
            sum_dices += random.randint(1, 6)
        return sum_dices

    def roll_the_dices(self, bets): # The function tells which customer won (ignoring minimum bet)
        draw = self.dices()
        winning_bets = [bet == draw for bet in bets]
        print("Rolling the dices...")
        print("the dices sum to %s." % str(draw))
        print("There are %s correct bets." % str(sum(winning_bets)))
        if any(winning_bets):
            customers = [i for i in enumerate(winning_bets)]
            print("Players number %s won." % str([x[0] + 1 for x in customers if x[1]]))
        else:
            print("No player won.")
        return winning_bets

    @staticmethod
    def compute_prize_factor(bets):  # Compute the prize factor that equally weights the winning probability for bets
        # on 2 dices and scales it in such away that on average 90% of the money goes back to the customers
        winning_prob = (6 - abs(bets - 7))/36
        prize_factor = round(0.9/winning_prob)
        return prize_factor

    def simulate_game(self, bets, betted_amounts): # The function returns the total amount won by the casino and a
        # list with the amounts won by the customers (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.roll_the_dices(bets)
        # prize_factor = 1  # Not necessary since correct price factor is computed above
        award = [round(valid * winning * amount * self.compute_prize_factor(Y)) for valid, winning, amount, Y in
                 zip(valid_bets, winning_bets, betted_amounts, bets)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]
