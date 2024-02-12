# tuples are similar to lists, but the elements can't be modified

# conventionally look like this:
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)  # round brackets
print(type(Fruit))

List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]  # list - square brackets
print(type(List_of_Fruit))

List_of_Fruit[0] = "Strawberries"  # can modifiy elements within list
print(List_of_Fruit)

# can't modify elements within tuple
# Fruit[0] = "Strawberries"
# print(Fruit)

# can perform similar operations on tuples to lists
print(Fruit[0:3])  # slicing
print(Fruit[0])  # recalling elements

# concatenation of tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# tuples with one element
x = (5)
print(type(x))
x = (5, )  # notation of tuple with one element
print(type(x))

print(len(Fruit))

# creating a tuple
another_tuple = tuple(("Hello", 18, True))  # can have any type in tuple
print(type(another_tuple))

# converting a tuple to a list and back
Fruit = list(Fruit)
print(type(Fruit))
Fruit.append("Pears")
print(Fruit)
Fruit = tuple(Fruit)
print(type(Fruit))

# unpacking a tuple
Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
print(len(Fruit))
(one, *two, three) = Fruit  # assigns variables to each element
print(one)
print(two)
print(three)  # asterisk assigns rest of list to that variable
# print(tuple(three))

# incorporate loops into tuples
for i in range(len(Fruit)):
    print(Fruit[i])
