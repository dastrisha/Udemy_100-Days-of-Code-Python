"""You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this."""

"""My Solution to this problem is given below"""


import random

rps_list=["rock", "paper", "scissors"]
computer_choice = random.choice(rps_list)

my_choice =input("What is your choice? Type 0 for rock, 1 for paper and 2 for scissors: ")
print()

#User input is a string with 0, 1 or 2. We need to convert these numbers to string rock paper scissor so that we can make a direct comparision with each element in the rps_list.
if my_choice == "0":
    my_choice_str = "rock"
    print (f"My choice:{my_choice_str}\n")
elif my_choice == "1":
    my_choice_str = "paper"
    print (f"My choice:{my_choice_str}\n")
elif my_choice == "2":
    my_choice_str = "scissors"
    print (f"My choice:{my_choice_str}\n")
else:
    print ("Invalid choice. Try again!\n")

#Conditional statements comparing the players choice with the computer choice.
if my_choice_str==computer_choice:
    print(f"Computer choice:{computer_choice}", "\nIt's a draw!\n")
elif computer_choice == rps_list[0] and my_choice_str== rps_list[2]:
    print(f"Computer choice:{computer_choice}","\nComputer wins!\n")
elif computer_choice == rps_list[1] and my_choice_str== rps_list[0]:
    print (f"Computer choice:{computer_choice}", "\nComputer wins!\n")
elif computer_choice == rps_list[2] and my_choice_str ==rps_list[1]:
    print (f"Computer choice:{computer_choice}", "\nComputer wins!\n") 
else:
    print(f"Computer choice:{computer_choice}","\nYou win!\n")





"""UDEMY Solution to this problem is given below"""
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
# if user_choice < 0 or user_choice > 2:
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

