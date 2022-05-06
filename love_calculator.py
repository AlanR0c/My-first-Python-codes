# Love Calculator #

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_name1 = name1.lower() 
lower_name2 = name2.lower()
#Here I've used the lower() function so that whatever the user types, it won't affect the program for the .lower() function gets all the letters transformed into lower case letters.

luv_1 = str(lower_name1.count('t') + lower_name1.count('r') + lower_name1.count('u') + lower_name1.count('e') + lower_name2.count('t') + lower_name2.count('r') + lower_name2.count('u') + lower_name2.count('e')) 

luv_2 = str(lower_name1.count('l') + lower_name1.count('o') + lower_name1.count('v') + lower_name1.count('e') + lower_name2.count('l') + lower_name2.count('o') + lower_name2.count('v') + lower_name2.count('e'))
#Here I've used the count() function, and what this function does is it returns the total count of a given element in a string, in this case we're counting the number of times the letters 't', 'r', 'u', 'e', 'l', 'o', 'v', 'e'(true love) appear given the user's input.

result = int(luv_1 + luv_2)

if result > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 89 or result >= 40:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")


# Luv Calculator 2.0 #

#This is a way more effective code using the random module

print("Welcome to the Love Calculator")
lovers = input("Please enter yer name and yer luv's name, will ye? \n")
love_score = random.randint(1, 100)

if love_score >= 85:
  print(f"Your score is {love_score}. Ye guys are soul mates!")
elif love_score <= 84 and love_score >= 60:
  print(f"Your score is {love_score}. Ye guys are meant to be together!")
elif love_score <= 59 and love_score >= 40:
  print(f"Your score is {love_score}. Ye guys are okayish.")
else:
  print(f"Your score is {love_score}. Er...ye guys should find sb else :/")  
