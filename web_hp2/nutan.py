import turtle
#khoi toa man hinh do hoa
screen = turtle.Screen()
#thiet lap do rong man hinh
screen.setup(500,500)
#thiet lap hinh anh nen
screen.bgpic('giphy.gif')
turtle.shape('triangle')
turtle.color('white')
#thiet lap toc do di chuyen cua nhan vat
move_speed=10
turn_speed=10
#thiet lap ham dieu khien
def foward():
    turtle.foward(move_speed)
def backward():
    turtle.backward(move_speed)
def left():
    turtle.left(move_speed)
def right():
    turtle.right(move_speed)
turtle.penup()#thiet lap khong gian ve khi di chuyen

#goi ham khi nhan cac phim tuong ung
screen.onkey(foward,'Up')
screen.onkey(backward,'Down')
screen.onkey(left,'Left')
screen.onkey(right,'Right')
screen.listen()
