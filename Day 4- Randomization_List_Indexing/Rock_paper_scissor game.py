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

