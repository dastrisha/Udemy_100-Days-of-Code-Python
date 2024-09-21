
"""Randomly scramble letters in a word, and the player has to guess the original word. Use a for loop to shuffle the letters and functions to manage the game flow."""

#MY CODE:

import random

word_list = ["apple","planet","orange","python","guitar","flower","jungle","mountain","computer","rocket","puzzle","sunshine",
"diamond","ocean","forest","castle","volcano","elephant","island","butterfly"]

print ("Welcome to the World Scramble Game!\nTry to guess the scrambled word or hit Exit to Quit.\n")


# Select a random word from the list
random_word = random.sample(word_list,1)

#Join the random word in a list into string
str_random_word = "".join(random_word)

#Writing a function to call scramble words
def scrambled_word():
   
    #scramble the selected word
    sc_word = random.sample(str_random_word, len(str_random_word))
    #Join the scrabmled letters back into string
    str_sc_word = "".join(sc_word)   
 
    return str_sc_word

print("Scrambled word is: ", scrambled_word())
print(str_random_word)

#Ask user to type the guessed word

user_input = input("Your guess: ").lower()

guess = 0

while user_input != str_random_word :
    print ("Incorrect! To try again type Try, to quit type Quit")
    user_action = input(" Try or Quit?: ").lower()
    if user_action == "try" :
            user_input = input("Your guess: ")
            guess = guess + 1

    elif user_action == "quit":
        print ("End Game")

        break
    
    else:
        print ("Incorrect Input. Try again! ")

# user enters correct input
if user_input == str_random_word :
    print("Correct. Well Done!")
    #Display the number of attempt to get the correct answer
    print(f"The number of attempts to guess the word correctly is {guess}")

     
#Recomended code:


import random

# List of words for the game
word_list = [
    "apple", "planet", "orange", "python", "guitar", "flower",
    "jungle", "mountain", "computer", "rocket", "puzzle", "sunshine",
    "diamond", "ocean", "forest", "castle", "volcano", "elephant",
    "island", "butterfly"
]

def scramble_word(word):
    """Scramble the selected word."""
    sc_word = random.sample(word, len(word))  # Scramble the word
    return "".join(sc_word)  # Return the scrambled word as a string

def play_game():
    """Main function to run the game."""
    random_word = random.choice(word_list)  # Select a random word
    scrambled = scramble_word(random_word)  # Scramble the selected word

    print("Welcome to the World Scramble Game!")
    print("Try to guess the scrambled word or type 'Quit' to exit.")
    print("Scrambled word is:", scrambled)

    guess_count = 0  # Initialize guess count

    while True:
        user_input = input("Your guess: ").lower()
        
        if user_input == "quit":
            print("End Game")
            break  # Exit the loop if the user wants to quit
        elif user_input == random_word:
            guess_count += 1  # Increment guess count for a correct guess
            print("Correct. Well Done!")
            print(f"The number of attempts to guess the word correctly is {guess_count}.")
            break  # Exit the loop after the correct guess
        else:
            guess_count += 1  # Increment guess count for an incorrect guess
            print("Incorrect! Try again or type 'Quit' to exit.")

# Start the game
play_game()

