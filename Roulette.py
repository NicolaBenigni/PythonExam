print("Welcome to this evaluation exam, fasten you seat belt and be ready to take off")

# Import library called random
import random
# Fix a seed, say 3456, so that even random draws can be replicated
random.seed(3456)
# Test that the seed works correctly: expected outcome: 7, 8, 5, 3, 9
print(random.randint(1,10))
print(random.randint(1,10))

