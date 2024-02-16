valid = True
answer1 = ""
answer2 = ""

while valid:
    number = int(input("Enter your number: "))  # takes user input for number
    if number % 2 == 0:  # if number is divisible by 2
        print(number, "is even!")
    else:
        print(number, "is odd!")

    answer1 = input("Would you like to see the times table? yes or no: ")
    if answer1.lower() in "yes":  # if statement using string response
        print("The", number, "times table is:")
        for i in range(1, 11):  # prints times table of given number up to ten
            print(number, "multiplied by", i, "is:", number * i)

    answer2 = input("Would you like to see another number? yes or no: ")
    if answer2.lower() in "yes":
        valid = True
    else:
        valid = False  # won't repeat unless desired
