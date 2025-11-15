# PROJECT: PASSWORD GENERATOR

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

list_password = []

# Inserting random letters into list
for i in range(0, nr_letters):
    list_password.append(random.choice(letters))

# Inserting random numbers into list
for i in range(0, nr_numbers):
    list_password.append(random.choice(numbers))

# Inserting random symbols into list
for i in range(0, nr_symbols):
    list_password.append(random.choice(symbols))

# Shuffling the list to get a random password
random.shuffle(list_password)

# Converting the password from list to string
final_password = ""

for i in list_password:
    final_password += i

print(f"Your Final Password: {final_password}")
