
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

guess = input("Guess a letter: ").lower()

display = ""




# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
