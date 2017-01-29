import random

# This file contains the function that defines the behaviour and payoffs of employees and customers

# Create employee as a class and the croupiers and barmen each as a subclass


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