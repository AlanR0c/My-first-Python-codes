# Pizza Order #

print("Welcome to Python Pizza Deliveries!\n")
print("Python Pizza Deliveries Menu:\nSmall pizza $15\nMedium Pizza $20\nLarge pizza $25\nAdd some pepperoni to yer small pizza for only $2 and only $3 to yer medium or large pizza.\nAdd some extra cheese for only $1 :D\n")
size = input("What size pizza do you want? Small, medium or large?\n").lower()
add_pepperoni = input("Do you want pepperoni? Yes or no?\n").lower()
extra_cheese = input("Do you want extra cheese? Yes or no?\n").lower()

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
if size == "small" and add_pepperoni == "yes" and extra_cheese == "yes":
  bill = 15 + 2 + 1
  print(f"Your final bill is: ${bill}.")
elif size == "small" and add_pepperoni == "yes" and extra_cheese == "no":
    bill = 15 + 2
    print(f"Your final bill is: ${bill}.")
    
if size == "medium" and add_pepperoni == "yes" and extra_cheese == "yes":
   bill = 20 + 3 + 1
   print(f"Your final bill is: ${bill}.")
elif size == "medium" and add_pepperoni == "yes" and extra_cheese == "no":
    bill = 20 + 3
    print(f"Your final bill is: ${bill}.")

if size == "large" and add_pepperoni == "yes" and extra_cheese == "yes":
    bill = 25 + 3 + 1
    print(f"Your final bill is: ${bill}.")
elif size == "large" and add_pepperoni == "yes" and extra_cheese == "no":
    bill = 25 + 3
    print(f"Your final bill is: ${bill}.")      

if size == "small" and add_pepperoni == "no" and extra_cheese == "no":  
  print(f"Your final bill is: ${small_pizza}.")
elif size == "medium" and add_pepperoni == "no" and extra_cheese == "no":
  print(f"Your final bill is: ${medium_pizza}.")
elif size == "large" and add_pepperoni == "no" and extra_cheese == "no":
  print(f"Your final bill is: ${large_pizza}.")
