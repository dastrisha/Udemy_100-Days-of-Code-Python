"""The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
The objective is to take the inputs from the user to these questions and then generate a random password. 
Use your knowledge about Python lists and loops to complete the challenge."""


#MY SOLUTION


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))

#Use random sample to ramdomly select multiple letters for the list. We didnt use random.choice since that lets us select only 1 element
random_letters= random.sample(letters, nr_letters)
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Use random sample to ramdomly select multiple symbols for the list.
random_symbols= random.sample(symbols, nr_symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Use random sample to ramdomly select multiple numbers for the list.
random_numbers= random.sample(numbers, nr_numbers)

#Generate password by concatenating the list of letters, symbols and numbers
ordered_password = random_letters + random_symbols + random_numbers

#To rearrange all characters randomly, find length of the list so that ramdom.sample instead of picking a subset randomly , picks all characters. 
str_password_len = len(ordered_password)

#rerrage the elements in the list
random_password = random.sample(ordered_password,str_password_len)

#combine the elements without brackets or "," into a string of characters using .join()
print ("Your password is: ", "".join(random_password))


#UDEMY SOLUTION


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random  # Import the random module to use its functions

# Initialize an empty list to store the password characters
password_list = []

# Loop to add random letters to the password_list
for char in range(0, nr_letters):   #range(start,stop)
    password_list.append(random.choice(letters))  # Select a random letter and append it to the list

# Loop to add random symbols to the password_list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))  # Select a random symbol and append it to the list

# Loop to add random numbers to the password_list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))  # Select a random number and append it to the list

# Print the password list before shuffling (optional, for debugging purposes)
print(password_list)

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Print the password list after shuffling (optional, for debugging purposes)
print(password_list)

# Initialize an empty string to hold the final password
password = ""

# Loop through the shuffled password_list and concatenate each character to the password string
for char in password_list:
    password += char

# Print the final password
print(f"Your password is: {password}")
