# Rollercoaster tickets 4.0 #

#This program uses some logical operators.


print("Welcome to our fuckin brilliant rollercoaster!\n")

height = int(input("Please enter yer height in cm:\n"))

if height >= 120:
  print("Fasten yer seatbelts, clench yer buttocks, it's going to be a bumpy ride :D\n")

  age = int(input("Please enter yer bloody age, will ye?\n"))

  if age >= 60:# or age == 55:
    print("Ye got a free ride on us :)")

  elif age >= 18:# or age == 44:
    print("Adult tickets are $12.")
  elif age >= 12:# or age == 17:
    print("Youth tickets are $7.")
  else:
    print("Child tickets are $5.")

  
  picture = input("Would ye like to have a pic taken, so that ye will be able to remember this mental moment forever? Type yes or no, please.\n").lower()
  adult_price = 12 + 3
  youth_price = 7 + 3
  child_price = 5 + 3
  
  if picture == "yes" and age >= 60:# or age == 55:
    print("Since you got a free ride on us, you only got to pay $3 for the picture. Enjoy the ride :D")
  elif picture == "yes" and age >= 18:# or age == 44:
    print(f"The ticket and the photo amount to ${adult_price}. Enjoy the bloody ride :D")  
  elif picture == "yes" and age >= 12 :#or age == 17:
    print(f"The ticket and the photo amount to ${youth_price}. Enjoy the bloody ride :D")  
  elif picture == "yes" and age <= 11:
    print(f"The ticket and the photo amount to ${child_price}. Enjoy the bloody ride :D")
  
  else:
    print("Enjoy the bloody ride :D")
  

else:
  print("Ye must grow taller before ye can ride. Now, bugger off ye midget.")
