from random import randint

# all upper case password
password = ""
for i in range(10):
    i = chr(randint(65, 90))  # values for letters in uppercase
    password = str(password) + i
print(password)

# alternate upper and lower
password = ""
for i in range(5):
    i = chr(randint(65, 90))  # upper case characters
    for j in range(5):
        j = chr(randint(65, 90)).lower()  # lower case characters
    password = str(password) + i + j
print(password)
