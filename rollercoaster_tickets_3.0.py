# Rollercoaster tickets 3.0 #

#This program uses multiple if statements in succession


#This program asks whether the user wants a picture. If they say yes, then we'll add $3 to the final price, and if  the answer is no, we give them the final price without the additional $3.


print("Welcome to our fuckin brilliant rollercoaster!\n")

height = int(input("Please enter yer height in cm:\n"))

if height >= 120:
  print("Fasten yer seatbelts, clench yer buttocks, it's going to be a bumpy ride :D\n")

  age = int(input("Please enter yer bloody age, will ye?\n"))

  if age >= 18:
    print("Adult tickets are $12.")
  elif age >= 12:
    print("Youth tickets are $7.")
  else:
    print("Child tickets are $5.")
  
  picture = input("Would ye like to have a pic taken, so that ye will be able to remember this mental moment forever? Type yes or no, please.\n").lower()
  adult_price = 12 + 3
  youth_price = 7 + 3
  child_price = 5 + 3
  if picture == "yes" and age >= 18:
    print(f"The ticket and the photo amount to ${adult_price}. Enjoy the bloody ride :D")
  elif picture == "yes" and age >= 12:
    print(f"The ticket and the photo amount to ${youth_price}. Enjoy the bloody ride :D")
  elif picture == "yes" and age <= 11:
    print(f"The ticket and the photo amount to ${child_price}. Enjoy the bloody ride :D")
  else:
    print("Enjoy the bloody ride :D")  

else:
  print("Ye must grow taller before ye can ride. Now, bugger off ye midget.")
