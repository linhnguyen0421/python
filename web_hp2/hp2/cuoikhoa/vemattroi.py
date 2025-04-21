import turtle

ninja = turtle.Turtle()

ninja.speed(30)
ninja.pencolor("yellow")
for i in range(180):
    ninja.forward(50)
    ninja.right(30)
    ninja.forward(10)
    ninja.left(60)
    ninja.forward(20)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
ninja.done()