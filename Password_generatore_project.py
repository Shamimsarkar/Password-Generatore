import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Make one empty list to store password

final_password = []

# Set initial value 0 for all combination

initial_letter = 0
initial_symbol = 0
initial_number = 0

# Print the sentence you what to show in screen

print("Welcome to the PyPassword Generator!\n")

# Take the input from user how many combination they want to use

numbers_of_letters = int(input("How many letters would you like in your password?\n"))
numbers_of_symbols = int(input("How many symbols would you like?\n"))
numbers_of_numbers = int(input("How many numbers would you like?\n"))

# Make shuffle all initial assign values so that your result give you random output

random.shuffle(letters)
random.shuffle(symbols)
random.shuffle(numbers)

# For loop to how many letters you want to use and place them in your empty list

for letter in letters:
    if initial_letter < numbers_of_letters:
        initial_letter +=1
        final_password.append(letter)

# For loop to how many symbols you want to use and place them in your empty list

for symbol in symbols:
    if initial_symbol < numbers_of_symbols:
        initial_symbol +=1
        final_password.append(symbol)

# For loop to how many numbers you want to use and place them in your empty list

for number in numbers:
    if initial_number < numbers_of_numbers:
        initial_number +=1
        final_password.append(number)

# again shuffle your final value otherwise it show numbers or letter one after one

random.shuffle(final_password)

# Finally print the final password you generated
print(final_password)

# Make the password in string form

final_password = "".join(final_password)

print(f"Your password is: {final_password}")
