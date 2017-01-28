import itertools
import random


random.seed(3456)


print("Test 1")

bets = [11, 15, 10, 20, 5]
above = [bet >= 10 for bet in bets]
print(above)
print(any(bets))


print("Test 2")

# award = "default"
# print(award)

# prize = float(award) * 30
# print(prize)

print("Indeed does not work")


print("Test 3")

print(random.randint(1, 36))


print("Test 4")

sum_dices = 0
for i in range(2):
    sum_dices += random.randint(1, 6)
print(sum_dices)

list_of_values = [random.randint(1, 6) for i in range(5)]
list_of_values2 = [random.randint(1, 6)+random.randint(1, 6) for i in range(5)]


#for i in range(10):
#    list_of_values = list_of_values.append(float(sum_dices))

#five_random_integers = [random.randint(1, 10) for _ in itertools.repeat(None, 5)]
#print(five_random_integers)


print(list_of_values)

print(list_of_values2)