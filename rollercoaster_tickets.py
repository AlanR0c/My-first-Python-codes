# Rollercoaster tickets #

#This program uses nested if/else

print("Welcome to the most brilliant rollercoaster in town :D")

height = int(input("Please enter yer height in cm:\n"))

if height >= 120:
  print("Ye can ride our rollercoaster. It's going to be a mental ride :D")
  age = int(input("Please enter yer age, will ye?\n"))
  if age <= 18:
    print("Ye got to pay $7.")
  else:
    print("Ye got to pay $12")

else:
  print("Ye got to grow a tad more, come back next year :(")     
