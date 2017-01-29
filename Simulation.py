# Import necessary libraries
from matplotlib import pyplot as plt
from random import randint
# Import the file "Roulette" where roulette and craps games are defined
import Roulette

# First 2 simulations of roulette games (numbers slightly different than in the powerpoint)
bets1 = [14, 14, 36, 0, 11, 14]
amounts1 = [10, 100, 120, 65, 150, 122]
table1 = Roulette.Roulette(100)
print(table1.simulate_game(bets1, amounts1))
print(table1.simulate_game(bets1, amounts1))

# First 2 simulations of craps games
bets2 = [8, 8, 10, 2, 3, 8]
amounts2 = [10, 120, 100, 65, 100, 100]
table2 = Roulette.Craps(100)
print(table2.simulate_game(bets2, amounts2))
print(table2.simulate_game(bets2, amounts2))

# Create a list that takes the values of 1000 throws of dice pairs (set at only 10 simulation)
list_of_values = []
for i in range(10):
    list_of_values.append(table2.dices())

# Print figures # (they are commented out because the code does not work on my pc)
# plt.hist(list_of_values)
# plt.show()
print(list_of_values)  # This is here to see the value that should enter the graph

# Simulate the craps game 1000 times and create a list of customers' and casino's results
# to show allocation of betted amounts chosen between 100 to 500 (set at only 10 simulation)
list_of_profit = []
list_of_awards = []
profit_over_betted_amounts = []
for i in range(10):
    bets3 = [randint(2, 12) for k in range(10)]
    amounts3 = [randint(100, 500) for j in range(10)]
    result = table2.simulate_game(bets3, amounts3)
    list_of_profit.append(result[0])
    list_of_awards.append(result[1])
    profit_over_betted_amounts.append(result[0]/sum(amounts3))

# Print figures
# plt.hist([item for sublist in list_of_awards for item in sublist])
# plt.hist(profit_over_betted_amounts)
# plt.show()
print([item for sublist in list_of_awards for item in sublist])  # This is here to see the value that should enter the graph
print(profit_over_betted_amounts)  # This is here to see the value that should enter the graph

# Print the average share of profit over the betted amount that the casino cashes in. The result is close to 0.10, which
# shows the correct programming of the prize factor
casino_avg_share = sum(profit_over_betted_amounts)/len(profit_over_betted_amounts)
print(casino_avg_share)

