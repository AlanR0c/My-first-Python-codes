# Rollercoaster tickets 2.0 #

#This program uses if/elif/else


print("Welcome to the fookin rollercoaster.\n")

height = int(input("Please enter yer height in cm\n"))


if height >= 120:
  print("Prepare yerself, it's going to be a neck-breaking ride.\n")
  age = int(input("Please inform yer ruddy age, will ya?\n"))
  if age >= 69:
    print("Sorry, we don't want ya to have a heart attack :/")
  elif age >= 19:
      print("Ye got to pay $20.")
  elif age > 11:
      print("Ye got to pay $15.")
  else:
      print("Ye got to pay only $10.")
else:
  print("Ye got to grow taller before ye can go for a ride on our rollercoaster.")
