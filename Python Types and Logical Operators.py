# Python Types

print(type("Hello, world!"))  # string
print(type(13))  # integer
print(type(4.72))  # float
print(type(True))  # bool

# moving to integers
print(4.72, int(4.72))  # always rounds down
print(4.05, int(4.05))

# rounding up
print(4.72, int(4.72), int(round(4.72)))

# moving strings to integers
print("12345", int("12345"))
print(type("12345"))
print(type(int("12345")))

# moving to floats
print(float(18))
print(float("12345"))

# moving to strings
print(str(18))
print(str(19.5))
print(type(str(19.5)))

# logical operators
# 3 different logical operators - "and", "or", "not"

x = 6
print(x > 0 and x < 10)  # 0 < x < 10

y = 23
print(y % 2 == 0 or y % 3 == 0)


