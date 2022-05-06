# Even or odd number #


#This program checks if a number is odd or even from the user's input using the modulo


number = int(input("Which number do you want to check? "))

calculation = number % 2

if calculation == 1:
  print("It's an odd number.")
else:
  print("It's an even number.")
