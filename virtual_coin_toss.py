#Virtual Coin Toss

#Here I used the .capitalize() method, which's sort of the opposite of the .lower() method.

import random

print("Welcome to the Virtual Coin Toss :D \n\n")

user_input = input("To toss the coin, please type Heads or Tails. \n")

coin = random.randint(0, 1)

if coin == 1:
  print("heads".capitalize())
else:
  print("tails".capitalize())
#print(coin)
