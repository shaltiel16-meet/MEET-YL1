import turtle
global curshape
global curcolor		
curshape="circle"
curcolor="pink"

turtle.speed(0)
turtle.hideturtle()
#drawing the outline
turtle.penup()
turtle.goto (-250,250)
turtle.pendown()
turtle.goto(-250,-250)
turtle.goto(250,-250)
turtle.goto(250,250)
turtle.goto(-250,250)

#drawing the color squares
def colorsquare(x,y,color):
	turtle.penup()
	turtle.goto(x,y)
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.pendown()
	turtle.goto(x,y-50)
	turtle.goto(x+50,y-50)
	turtle.goto(x+50,y)
	turtle.goto(x,y)
	turtle.end_fill()
colorsquare(200,250,"pink")
colorsquare(200,200,"blue")
colorsquare(200,150,"red")
turtle.penup()
turtle.goto(225,50)
turtle.pendown()
turtle.circle(25)
turtle.goto(250,50)
turtle.goto(250,-5)
turtle.goto(200,-5)
turtle.goto(200,50)
turtle.goto(225,50)




turtle.pencolor("yellow")
colorsquare(200,250,"pink")
turtle.penup()
turtle.goto(225,50)
turtle.pendown()
turtle.circle(25)

def userclicked (x,y):
	global curcolor
	global curshape
	if (x>=200 and x<=250 and y<=250 and y>=200):
		turtle.pencolor("black")
		colorsquare(200,200,"blue")
		colorsquare(200,150,"red")
		turtle.pencolor("yellow")
		colorsquare(200,250,"pink")
		curcolor="pink"
	elif (x>=200 and x<=250 and y<=200 and y>=150):
		turtle.pencolor("black")
		colorsquare(200,250,"pink")
		colorsquare(200,150,"red")
		turtle.pencolor("yellow")
		colorsquare(200,200,"blue")
		curcolor="blue"
	elif (x>=200 and x<=250 and y<=150 and y>=100):
		turtle.pencolor("black")
		colorsquare(200,200,"blue")
		colorsquare(200,250,"pink")
		turtle.pencolor("yellow")
		colorsquare(200,150,"red")
		curcolor="red"
	elif (x>=200 and x<=250 and y<=100 and y>=50):
		turtle.pencolor("black")
		turtle.penup()
		turtle.goto(250,50)
		turtle.pendown()
		turtle.goto(250,-5)
		turtle.goto(200,-5)
		turtle.goto(200,50)
		turtle.goto(225,50)
		turtle.pencolor("yellow")
		turtle.penup()
		turtle.goto(225,50)
		turtle.pendown()
		turtle.circle(25)
		curshape="circle"
	elif (x>=200 and x<=250 and y<=50 and y>=0):
		turtle.pencolor("yellow")
		turtle.penup()
		turtle.goto(250,50)
		turtle.pendown()
		turtle.goto(250,-5)
		turtle.goto(200,-5)
		turtle.goto(200,50)
		turtle.goto(225,50)
		turtle.pencolor("black")
		turtle.penup()
		turtle.goto(225,50)
		turtle.pendown()
		turtle.circle(25)
		curshape="square"
	else:
		print(curcolor)
		turtle.pencolor(curcolor)
		turtle.fillcolor(curcolor)
		turtle.penup()
		turtle.goto(x,y)
		turtle.pendown()
		turtle.begin_fill()
		if (curshape=="circle"):
			turtle.circle(10)
		else: 
			turtle.goto(x+10,y)
			turtle.goto(x+10,y+20)
			turtle.goto(x-10,y+20)			
			turtle.goto(x-10,y)
			turtle.goto(x+10,y)
		turtle.end_fill()
turtle.onscreenclick(userclicked)




turtle.mainloop()
