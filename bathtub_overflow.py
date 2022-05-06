# Bathtub overflow #


# This program measures the volume of water in a bathtub. If the water lever reaches the overflow drain, then it stops filling it up. If not, it carries on till the level of water reaches the overflow limit.


import random

water_level = random.randint(0, 100)
if water_level > 80:
  print("Overflow activated")
else:
  print("Bathtub being filled up")
