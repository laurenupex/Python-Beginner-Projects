# drawing with turtle package

# import turtle
import turtle

# setup in turtle
turtle.bgcolor("black")  # bg colour
turtle.pensize(2)  # pen size
turtle.color("green")
turtle.speed(0)

# draw a square
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # allows turtle to stay on screen

# draw a pattern
# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
    # turtle.color(colours)
   # turtle.circle(150)
  #  turtle.left(10)
# turtle.done()

# make it cooler
for i in range(12):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()
