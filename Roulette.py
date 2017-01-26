# Import libraries called intertools and random
import itertools
import random

# Fix a seed, say 3456, so that even random draws can be replicated
random.seed(3456)

# Test whether the seed works correctly: expected random outcome: 7, 8, 5, 3, 9
five_random_integers = [random.randint(1, 10) for _ in itertools.repeat(None, 5)]
print(five_random_integers)

