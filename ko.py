import turtle

turtle.speed(0)
turtle.bgcolor("white")
turtle.pencolor("MediumAquamarine")

h = 10

for j in range(360):

    for i in range(4):
        turtle.forward(h)
        turtle.right(90)
    turtle.right(3)
    h = h * 1.01
