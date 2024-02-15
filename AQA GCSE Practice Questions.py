# # a program to determine how old you will be on your next birthday
#
# current_age = int(input("Enter your current age: "))  # takes current age of user
# next_birthday = current_age + 1  # adds 1 year to current age
# print("You will be", next_birthday, "years old on your next birthday!")  # outputs age at next birthday
#
# # a program to calculate the volume of a rectangular swimming pool with a depth of two metres
# pool_length = int(input("Enter the length of the pool in metres: "))
# pool_width = int(input("Enter the width of the pool in metres: "))
# pool_volume = pool_width * pool_length * 2
# print("The volume of the pool is", pool_volume, "m^3")
#
# # The OR logic gate outputs a 1 if either of the two inputs are 1, otherwise it will output a 0
# input1 = int(input("Enter a digit, either 1 or 0: "))
# while input1 > 1 or input1 < 0:
#     input1 = int(input("Sorry, value is not either 0 or 1. Please reenter: "))
#
# input2 = int(input("Enter a digit, either 1 or 0: "))
# while input2 > 1 or input2 < 0:
#     input2 = int(input("Sorry, value is not either 0 or 1. Please reenter: "))
#
# if input1 == 1 or input2 == 1:
#     print("1")
# else:
#     print("0")

# Write a Python program that plays the following number guessing game.
# Your program should:
# • randomly generate a 2 digit numeric code (ie numbers between 10 and 99)
# • allow the user 10 turns to guess the code as follows:
# o prompt the user to enter a 2 digit number (validation is not required)
# o calculate the number of correct digits in the correct place
# o output a suitable message followed by the number of correct digits in the correct
# place
# • output a suitable message if the user has guessed the 2 digit code correctly within 10 turns
# • output a suitable message along with the correct code if the user has had 10 turns and
# failed to guess the code correctly.

from random import randrange
numeric_code = randrange(10, 99)
numeric_code = str(numeric_code)
guess = ""
correct_digits = 0
number_of_guesses = 0

while number_of_guesses < 10:
    guess = input("Please guess the 2-digit numeric code between 10 and 99: ")
    correct_digits = 0
    number_of_guesses = number_of_guesses + 1
    if guess == numeric_code:
        print("You correctly guessed the code, well done!")
        number_of_guesses = 11
    else:
        if guess[0] == numeric_code[0]:
            correct_digits = correct_digits + 1
        if guess[1] == numeric_code[1]:
            correct_digits = correct_digits + 1
        if correct_digits > 0:
            print("There are", correct_digits, "correct digits.")
        else:
            print("Neither digit is correct.")

if guess != numeric_code:
    print("Sorry, you did not guess the code within 10 tries. The correct code was", numeric_code)
