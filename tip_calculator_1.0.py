##Tip Calculator 1.0 ##

print("Welcome to the Tip Calculator")

bill = input("What was the total bill? $")
percentage = input("What percentage tip would like to give? 10, 12 or 15? ")

number_of_people = input("How many people to split the bill? ") 

bill_float = float(bill)
percentage_int = int(percentage)
number_of_people_int = int(number_of_people)

percent_10 = (bill_float / number_of_people_int) * 1.10
percent_12 = (bill_float / number_of_people_int) * 1.12
percent_15 = (bill_float / number_of_people_int) * 1.15

if percentage_int == 10 :
    print(f"Each person should pay $ {round(percent_10, 2)}")

elif percentage_int == 12 :
  print(f"Each person should pay $ {round(percent_12, 2)}")
else :
  print(f"Each person should pay $ {round(percent_15, 2)}")
