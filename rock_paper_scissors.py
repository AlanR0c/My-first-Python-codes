# Rock Paper Scissors #

print("Welcome to our Rock Paper Scissors game :D")
user_choice = int(input("Please enter 0 to choose rock, 1 to choose paper and 2 to choose scissors \n"))
#magic_list = user_choice.split(", ")
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if user_choice >= 3 or user_choice < 0:
  print("You've typed an invalid number, please try again.")
#Initially, me program didn't have this condition, meaning that if the user typed any number other than the ones displayed at the beginning, it'd crash the program.  
decision_list = [rock, paper, scissors]
contest = random.randint(0, len(decision_list) - 1)
#Alternatively, I could've just coded like so:
#contest = random.randint(0, 2)

#contest1 = decision_list[user_choice]
#rock = 0
#battle = [rock]2
#print(contest)


if user_choice == 0 and contest == 1:
  print(f"You chose:{rock}\nComputer chose:{paper}\nYou lose.")
elif user_choice == 0 and contest == 2:
  print(f"You chose:{rock}\nComputer chose:{scissors}\nYou win.")      
elif user_choice == 1 and contest == 2:
  print(f"You chose:{paper}\nComputerchose:{scissors}\nYou lose.")   
elif user_choice == 1 and contest == 0:
  print(f"You chose:{paper}\nComputer chose:{rock}\nYou win.")
elif user_choice == 2 and contest == 0:
  print(f"You chose:{scissors}\nComputer chose:{rock}\nYou lose.")
elif user_choice == 2 and contest == 1:
  print(f"You chose:{scissors}\nComputer chose:{paper}\nYou win.")
elif user_choice == 0 and contest == 0:
  print(f"You chose:{rock}\nComputer chose:{rock}\nIt's a draw.")
elif user_choice == 1 and contest == 1:
  print(f"You chose:{paper}\nComputer chose:{paper}\nIt's a draw.") 
elif user_choice == 2 and contest == 2:
  print(f"You chose:{scissors}\nComputer chose:{scissors}\nIt's a draw.")
