# Import necessary libraries
import random
from random import randint

### This file contains the function that defines the behaviour and payoffs of employees and customers

# Create employee as a class and croupier and barman each as a subclass

class Employee(object):
    def __init__(self, wage=200):
        self.wage = wage


class Croupier(Employee):
    def __init__(self, wage=200, fee=0):
        super(Croupier, self).__init__(wage)  # This is to inherit the fixed wage defined before, since same for both
        # croupiers and barmen
        self.fee = fee


class Barman(Employee):
    def __init__(self, wage=200, sales=0, tips=0):
        super(Barman, self).__init__(wage)  # This is to inherit the fixed wage defined before, since same for both
        # croupiers and barmen
        self.sales = sales
        self.tips = tips


# Create customer as a class and returning, onetime and bachelor each as a subclass

class Customer(object):
    initial_lower_bound = 0
    initial_upper_bound = 0

    def __init__(self, amount=None, budget=0, drinks=0, tips=0, final_budget=0, barman: Barman=None):
        self.amount = amount  # The amount to be betted is chosen at random according to some rules. It is used in the Roulette file
        self.final_budget = final_budget  # Amount that the customer takes homes
        self.budget = budget
        self.drinks = drinks  # Expenditure on drinks
        self.tips = tips  # Tips given
        self.barman = barman  # The variable tells if a customer has a barman assigned or not
        self.initial_budget = budget  # The initial budget is set at random between an upper and a lower bound

    def set_initial_budget(self):  # The function sets the initial budget at random between two bounds
        self.budget = randint(self.initial_lower_bound, self.initial_upper_bound)
        self.initial_budget = self.budget  # Initially the budget correspond to the initial_budget and it will get updated later on

    def give_tip(self):  # The function assigns a random tip to the barman and deduce it from the customer's budget
        if self.budget >= 20:
            tip = randint(0, 20)
            self.barman.tips += tip
            self.tips += tip
            self.budget -= tip

    def buy_drinks(self):  # The function allows the customer to randomly buy 1 or 2 drinks from the barman
        if self.budget >= 60:
            drink_price = random.choice([20, 40])
            self.drinks += drink_price
            self.barman.sales += drink_price
            self.budget -= drink_price
            self.give_tip()
            return drink_price
        else:
            self.drinks += 0
            return 0

    def set_final_budget(self):  # The function determines the amount won by the customer
        self.final_budget = self.budget - self.initial_budget

class Returning(Customer):
    initial_lower_bound = 100
    initial_upper_bound = 300

    def place_amount(self, min_amount):  # The function is used in the Roulette file and it bets random amounts
        # for each customers depending on the type of customer
        if self.budget >= min_amount:
            self.amount = min_amount
            self.budget -= min_amount
        else:
            self.amount = 0

class Onetime (Customer):
    initial_lower_bound = 200
    initial_upper_bound = 300

    def place_amount(self):
        betting = randint(0, round(self.budget/3))
        self.amount = betting
        self.budget -= betting

class Bachelor(Customer):
    initial_lower_bound = 200
    initial_upper_bound = 500

    def place_amount(self):
        betting = randint(0, round(self.budget))
        self.amount = betting
        self.budget -= betting
