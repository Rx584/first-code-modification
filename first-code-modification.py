import turtle
penColorList = ["red","blue","yellow","green"]
pen = turtle.Pen()
pen.speed(0)

for i in range(500):
	pen.pencolor(penColorList[i%4])
	pen.forward(i)
	pen.left(100)
	pen.hideturtle()
turtle.done()
