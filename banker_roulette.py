#Banker Roulette - Who will pay the bill?

names_string = input("Give me everbody's names, separated by a comma: \n")
names = names_string.split(", ")

import random

loser_selection = random.randint(0, len(names)-1)
print(names[loser_selection] + " is going to pay for everybody today.")
#Alternatively, I could've printed the whole thing without creating a variable, as follows:
#print(names[random.randint(0, len(names) -1)])


#Banker Roulette - Using the .choice() function

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

import random

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
