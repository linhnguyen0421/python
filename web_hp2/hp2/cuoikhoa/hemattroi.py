import turtle
import random
from random import randint
e = turtle
e.screensize()
e.speed(999)
e.screensize(2000, 2000)
e.bgcolor('black')
e.color('yellow')
def vemattroi():
  for i in range(180):
    e.forward(50)
    e.right(30)
    e.forward(10)
    e.left(60)
    e.forward(20)
    e.right(30)
    
    e.penup()
    e.setposition(0, 0)
    e.pendown()
    
    e.right(2)
def vehanhtinh():
  e.up()
  e.setheading(0)
  e.home()
  e.forward(300)
  e.down()
  e.color('grey')
  e.width(20)
  e.circle(2)
  e.up()
  e.forward(100)
  e.colormode(255)
  for i in range (10):
    a = random.randint(0,10)
    b = random.randint(50,100)
    e.down()
    e.color(randint(0, 255),
         randint(0, 255),
         randint(0, 255))
    e.circle(a)
    e.up()
    e.forward(b)
def vengoisao():
  e.up()
  e.home()
  e.width(4)
  e.right(90)
  e.forward(1)
  e.left(90)
  for i in range (100):
    c = random.randint(1,2)
    d = random.randint (-900,900)
    h = random.randint (-900,900)
    e.goto(d,h)
    e.down()
    e.color('white')
    e.circle(c)
    e.up()
vemattroi()
vehanhtinh()
vengoisao()
turtle.done()