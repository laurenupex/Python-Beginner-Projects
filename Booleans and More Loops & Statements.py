# boolean = true or false

# print(True)
# print("True")

# print(type(True))  # type = bool
# print(type("True"))  # type = string

# testing true and false bools
# print(5 == 5)
# print(6 == 5)

# incorporating the if statement with booleans
x = 10
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# while loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1

# incorporating else statement in while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("Number is no longer less than 4")

# if statement
number = 1
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")