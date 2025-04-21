import turtle 

windows=turtle.Screen()
windows.title('San bong da')
windows.bgcolor('green')

t = turtle.Turtle()
t.shape('circle')
t.penup()
t.goto(0,-50)
t.pendown()
t.pensize(3)
t.color('white')
t.circle(50)

def duongbien():
  t.penup()
  t.goto(0,160)
  t.pendown()
  t.goto(0,-160)
  t.forward(250)
  t.left(90)
  t.forward(320)
  t.left(90)
  t.forward(500)
  t.left(90)
  t.forward(320)
  t.left(90)
  t.forward(250)

duongbien()

def benphai():
  t.penup()
  t.goto(250,30)
  t.pendown()
  t.forward(30)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(30)
  t.penup()
  
  t.goto(250,60)
  t.pendown()
  t.forward(50)
  t.left(90)
  t.forward(110)
  t.left(90)
  t.forward(50)
  t.penup()
  
  t.goto(250,90)
  t.pendown()
  t.left(180)
  t.forward(90)
  t.left(90)
  t.forward(170)
  t.left(90)
  t.forward(90)

benphai()

def penaltyphai():
  t.penup()
  t.goto(180,0)
  t.pendown()
  t.begin_fill()
  t.circle(2)
  t.end_fill() 
  
penaltyphai()

def bentrai():
  t.penup()
  t.goto(-250,30)
  t.pendown()
  t.left(180)
  t.forward(30)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(30)
  
  t.penup()
  t.goto(-250,60)
  t.pendown()
  t.forward(50)
  t.right(90)
  t.forward(110)
  t.right(90)
  t.forward(50)
  
  t.penup()
  t.goto(-250,90)
  t.pendown()
  t.left(180)
  t.forward(90)
  t.right(90)
  t.forward(170)
  t.right(90)
  t.forward(90)

bentrai()

def penaltytrai():
  t.penup()
  t.goto(-180,0)
  t.pendown()
  t.begin_fill()
  t.circle(2)
  t.end_fill() 
  t.penup()
  t.goto(0,0)

penaltytrai()

def di_len():
  t.setheading(90)
  t.forward(10)

def di_xuong():
  t.setheading(270)
  t.forward(10)

def sang_trai():
  t.setheading(180)
  t.forward(10)

def sang_phai():
  t.setheading(0)
  t.forward(10)

windows.listen()

windows.onkey(di_len, "Up")
windows.onkey(di_xuong, "Down")
windows.onkey(sang_phai, "Right")
windows.onkey(sang_trai, "Left")

windows.mainloop()