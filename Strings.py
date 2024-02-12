# integers, floats & booleans considered simple data types - can't be broken down
# lists and strings can be broken down - made up of smaller elements

# print("hello world")
# print(type("hello world"))
#
# # + sign concatenation
# Greeting = "Hello"
# Name = "Lauren"
# print(Greeting + Name)
#
# # * operator
# print(Name*3)
# print((Greeting + Name)*3)
#
# # index operator
# Name = "Brad"
# print(Name[2])
# print(Name[0] + Name[3])
#
# # slicing strings
# print(Name[1:3])
# print(Name[:3])
# print(Name[1:])
#
# Name = "Lauren"
# print(Name.lower())
# print(Name.upper())
#
# # count how many times a character appears in a string
# print(Name.count("a"))
#
# # replace specific characters with other characters
# print(Name.replace("en", "a"))
# Name = "Ellie"
# New_Name = Name.replace("l", "d")
# print(New_Name)
#
# # find length of string
# print(len(Name))
#
# # format strings
# Your_name = input("Your name: ")
# hello = "Hello {}".format(Your_name)
# print(hello)

# each letter in python assigned to a specific number
print("orange" < "strawberry")
print(ord("o"))  # prints number assigned to character o
print(chr(38))  # prints character with value of 38
print(ord("o") + ord("r") + ord("a") + ord("n") + ord("g") + ord("e"))

# in and not operators
fruit = "bananas"
print("a" in fruit)
print("s" not in fruit)

# incorporating
x = "hello"
y = " "
for character in x:
    y = character.upper() + y
print(y)
