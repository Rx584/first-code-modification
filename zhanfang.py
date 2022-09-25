import turtle
pen = turtle.Pen()
pen.speed(0)
pen.pencolor("red")
for i in range(500):

    pen.forward(i)
    pen.left(100)
    pen.hideturtle()
turtle.done()
