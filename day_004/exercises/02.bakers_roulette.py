# Banker Roulette
# Description
# Figure out how to pick a random name from the list of friends.

import random

friends = ["Alice","Bob","Charlie","David","Emanuel"]

#1 Option
random_position = random.randint(0,len(friends) - 1)

print(f"The bill will be paid from: {friends[random_position]}")

#2 Option
print(random.choice(friends))