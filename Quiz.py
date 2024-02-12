import turtle
import matplotlib.pyplot as plt

x = 3
y = 7
print(x + y)
print(x / y)
print(x - y)
print(x * y)

List = []
for i in range(101):
    if i % 2 == 0:
        List.append(i)
print(List)
print(List[0:10])
print(len(List))
List.append(101)
print(List)
# also - List = list(range(0, 101, 2))

a = 6
if a % 5 == 0:
    print(a, "is divisible by 5")
else:
    print(a, "is not divisible by 5")

for i in range(6):
    print(i)

for i in range(5):
    turtle.forward(50)
    turtle.left(72)
turtle.done()


def pythagorean(a, b, c):
    if c**2 == a**2 + b**2:
        return True
    else:
        return False


print(pythagorean(3, 4, 5))

# n = 5
# while n > 0
#     n = n + 1
#     print(n)
# missing colon, also continues indefinitely - n is always > 0 and keeps getting bigger

List1 = [1, 2, 3, 4, 5]
List2 = [6, 7, 8, 9, 10]
plt.plot(List1, List2, c="green", linewidth=1, label="A Line", linestyle="dashed",
         marker="s", markerfacecolor="purple", markersize=2)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Python plot of a line")
plt.legend()
plt.show()
