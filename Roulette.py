# Import library called random
import random

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

class Table(object):  # Start with Table as a class, Roulette is going to be a subclass. The table is characterized by the following elements: a game, a croupier and customers
    def __init__(self, min_amount=0, croupier=None, customers=None, profit=0):
        self.min_amount = min_amount
        self.customers = customers
        self.croupier = croupier
        self.profit = profit

    def above_minimum(self, betted_amounts):  # The function takes a list of betted amounts and returns a list of booleans
        valid_bets = [amount >= self.min_amount for amount in betted_amounts]
        return valid_bets

#    def simulate_game(self, bets, betted_amounts):  # The function can take a list of bets and betted amounts and return the amount won by casino and costumers automatically taking into account the type of game played





class Roulette(Table):
#    bet_range = range(0, 36)

#    def minimum_amount(self):  # The function determines the minimum amount to be betted in a roulette game
#        self.min_amount = random.choice([50, 100, 200])

    def spin_the_wheel(self, bets):  # The function tells which customer won (ignoring the minimum amount to be betted)
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

    def simulate_game(self, bets, betted_amounts):  # The function returns the total amount won by the casino and a list with the amounts won by the customers (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.spin_the_wheel(bets)
        prize_factor = 30
        award = [valid * winning * amount * prize_factor for valid, winning, amount in zip(valid_bets, winning_bets, betted_amounts)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]


# Create a craps game

class Craps(Table):
#    bet_range = range(2, 12)

#    def minimum_amount(self):  # The function determines the minimum amount to be betted in a craps game
#        self.min_amount = random.choice([0, 25, 50])

    def dices(self):  # The function rolls 2 dices and gives their sum
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

    def compute_prize_factor(self, bets):  # Compute the prize factor that equally weights the winning probabily for bets on 2 dices and scales it in such away that on average 90% of the money goes back to the customers
        winning_prob = (6 - abs(bets - 7))/36
        prize_factor = round(0.9/winning_prob)
        return prize_factor

    def simulate_game(self, bets, betted_amounts): # The function returns the total amount won by the casino and a list with the amounts won by the customers (taking into account the minimum amount to be betted)
        valid_bets = self.above_minimum(betted_amounts)
        winning_bets = self.roll_the_dices(bets)
        prize_factor = 1
        award = [round(valid * winning * amount * self.compute_prize_factor(Y)) for valid, winning, amount, Y in zip(valid_bets, winning_bets, betted_amounts, bets)]
        profit = sum(betted_amounts) - sum(award)
        return [profit, award]



