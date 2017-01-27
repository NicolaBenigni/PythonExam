import random

bets = [11, 15, 10, 20, 5]

above = [bet >= 10 for bet in bets]
print(above)


print(any(bets))



#award = "default"
#print(award)

#prize = float(award) * 30
#print(prize)


random.seed(3456)
print(random.randint(1, 36))

n = 2
sum_dices = 0
for i in range(n):
    sum_dices += random.randint(1, 6)

print(sum_dices)