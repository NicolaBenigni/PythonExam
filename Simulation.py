import Roulette

# First 2 simulations of roulette games (numbers slightly different than in the powerpoint)
bets1 = [14, 14, 36, 0, 11, 14]
amounts1 = [10, 100, 120, 65, 150, 122]
table1 = Roulette.Roulette(100)
print(table1.simulate_game(bets1, amounts1))
print(table1.simulate_game(bets1, amounts1))
