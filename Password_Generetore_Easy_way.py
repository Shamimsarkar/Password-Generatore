import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Make one empty list to store password

final_password = []

# Print the sentence you what to show in screen

print("Welcome to the PyPassword Generator!\n")

# Take the input from user how many combination they want to use

numbers_of_letters = int(input("How many letters would you like in your password?\n"))
numbers_of_symbols = int(input("How many symbols would you like?\n"))
numbers_of_numbers = int(input("How many numbers would you like?\n"))


for char in range(0, numbers_of_letters):
    final_password.append(random.choice(letters))

for char in range(0, numbers_of_numbers):
    final_password.append(random.choice(numbers))

for char in range(0, numbers_of_symbols):
    final_password.append(random.choice(symbols))

random.shuffle(final_password)

print(final_password)

print(f"Your final password is: {"".join(final_password)}")