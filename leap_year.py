# Leap year #

#These programs tell you whether a year, from the user's input, is a leap year.


year = int(input("Which year do ya want to check, eh?\n"))

if year % 400 == 0:
  print("It's a leap year.")
elif year % 100 == 0:
  print("It's not a leap year.")
elif year % 4 == 0:
  print("It's a leap year.")
else:
  print("It's not a leap year.")


#This is, perhaps, the most ideal code.

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It's a leap year.")
    else:
     print("it's not a leap year.")
  else:
   print("It's a leap year.")
else:
  print("It's not a leap year.")
