
# """Every step is a separate section in the this course"""


# """STEP 1"""

# import random
# word_list = ["aardvark", "baboon", "camel"]

# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Gusess a letter: ").lower()

# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.

# for char in chosen_word :
#     if guess == char :
#         print ("Right")
#     else:
#         print("wrong")


# """STEP 2"""

# # TODO-4: Create a "placeholder" with the same number of blanks as the chosen_word

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# guess = input("Guess a letter: ").lower()


# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)


"""STEP 3"""


import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.


#This initializes a boolean variable game_over to False.It's used as a condition for the while loop to keep the game running until the player wins by guessing all letters.
game_over = False

#An empty list correct_letters is created to store the letters that the player guesses correctly.This will help keep track of the guessed letters and update the displayed word accordingly.
corrected_letter = []  

#This is a while loop that will keep running as long as game_over is False.The game will continue until the player has guessed all the letters and game_over becomes True.
while not game_over : 

#The player is prompted to guess a letter using the input() function, which takes input from the user.
    guess = input("Guess a letter: ").lower()

#The display is an empty string will be updated each time to show the current state of the word with correctly guessed letters.
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrected_letter.append(guess)
        elif letter in corrected_letter:
            display += letter
        else:
            display+= "_"

    print(display)

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    if "_" not in display:
        game_over = True
        print("You win.")
