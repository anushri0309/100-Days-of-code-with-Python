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
choise=int(input("Which would you like to choose?Type 0 for Rock,1 for Paper,and 2 for Scissors  "))
if choise==0:
    print(rock)
elif(choise==1):
    print(paper)
elif(choise==2):
    print(scissors)
else:
    print("Wrong input")
comp=random.randint(0,2)
if comp==0:
    print("Computer:",rock)
elif comp==1:
    print("Computer:",paper)
else:
    print("Computer:",scissors)
if (comp == 0 and choise == 1) or (comp == 1 and choise == 2) or (comp == 2 and choise == 0):
    print("You Win!")
elif (comp == 1 and choise == 0) or (comp == 2 and choise == 1) or (comp == 0 and choise == 2):
    print("You Lose!")
elif(comp==choise):
    print("drow")
else:
    ("Incorrect option ")




OR 

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")