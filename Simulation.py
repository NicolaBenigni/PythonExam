# Import the file "Roulette" where roulette and craps games are defined
import Roulette
from matplotlib import pyplot as plt

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

# Create a list that takes the values of 1000 throws of dice pairs
list_of_values = []
for i in range(1000):
    list_of_values.append(table2.dices())

print(list_of_values)

# Print figures (they are commented out because the code does not work on my pc)
# plt.hist(list_of_values)
# plt.show()


