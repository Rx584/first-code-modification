import turtle
penColorList = ["red","blue","yellow","green"]
pen = turtle.Pen()
pen.speed(0)

for i in range(2500):
	pen.pencolor(penColorList[i%4])
	pen.forward(i/10)
	pen.left(100)
	pen.hideturtle()
pen.penup()
pen.goto(-200,-200)
pen.pd()
pen.pencolor("black")
pen.write("欲买桂花同载酒，终不似，少年时",font=("宋体",12,"normal"))
turtle.done()
