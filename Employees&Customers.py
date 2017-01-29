from random import randint


# This file contains the function that defines the behaviour and payoffs of employees and customers

# Create employees as a class and croupiers and barmen each as a subclass

class Employee(object):
    def __init__(self, wage=200):
        self.wage = wage


class Croupier(Employee):
    def __init__(self, wage=200, fee=0):
        super(Croupier, self).__init__(wage)  # This is to inherit the fixed wage defined before, since same for both croupiers and barmen
        self.fee = fee


class Barman(Employee):
    def __init__(self, wage=200, sales=0, tips=0):
        super(Barman, self).__init__(wage)  # This is to inherit the fixed wage defined before, since same for both croupiers and barmen
        self.sales = sales
        self.tips = tips


# Create customers as a class and returning, one-time and bachelor each as a subclass

class Customer(object):
    initial_lower_bound = 0
    initial_upper_bound = 0


class Returning(Customer):
    initial_lower_bound = 100
    initial_upper_bound = 300

    def place_random_amount(self, min_amount):  # The function is used in the Roulette file and it bets random amounts for each customers depending on the type of customer
        if self.budget >= min_amount:
            self.amount = min_amount
            self.budget -= min_amount
        else:
            self.amount = 0


class Onetime (Customer):
    initial_lower_bound = 200
    initial_upper_bound = 300

    def place_random_amount(self, _):
        betting = randint(0, round(self.budget/3))
        self.amount = betting
        self.budget -= betting


class Bachelor(Customer):
    initial_lower_bound = 200
    initial_upper_bound = 500

    def place_random_amount(self, _):
        betting = randint(0, round(self.budget))
        self.amount = betting
        self.budget -= betting
