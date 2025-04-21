
#chiến binh không gian
import turtle
import random
#thiet lap man hinh do hoa
sc= turtle.Screen()
#thiet lap hinh anh nen cho man hinh do hoa
sc.bgpic('vutru.gif')
#ve vung gioi han di chuyen
mypen = turtle.Turtle()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
#mypen.hiheturtle()

#tao ra nhan vat sieu anh hung
player=turtle.Turtle()
player.color('yellow')
player.shape('turtle')
player.penup()
# Tạo ra quái vật
goal = turtle.Turtle()
image="tau.gif"
sc.addshape(image)
goal.shape(image)
goal.penup()
goal.speed(0)

# hàm setposition() đặt đối tượng ở vị trí (x, y)

goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
#thiet lap tac do sieu anh hung
speed=1
#ham di chuyen
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increaseSpeed():
    global speed
    speed +=1
    if speed >=5:
        speed = 5
def decreaseSpeed():
    global speed
    speed -=1
    if speed <= -5:
        speed = -5

#khi nhan phim
turtle.listen()
turtle.onkey(turnleft,'Left')
turtle.onkey(turnright,'Right')
turtle.onkey(increaseSpeed,'Up')
turtle.onkey(decreaseSpeed,'Down')
# tao ham kiem tra cac nhan vat khi cham bien
def boundaryChecking(t):
    if (player.xcor()<-300) or (player.xcor()>300):
        player.right(180)
        t.setposition(random.randint(-300,300),random.randint(-300,300))
    if (player.ycor()<-300) or (player.ycor()>300):
        player.right(180)
        t.setposition(random.randint(-300,300),random.randint(-300,300))
#kiem tra va cham
def isCollision(t1,t2):
    #khoang cach giua sieu anh hung va quai vat
    '''d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False'''
while True:
    player.forward(speed)
    # thiết lập quái vật di chuyển
    goal.forward(10)
    goal.left(random.randint(10,180))
    # kiểm tra siêu anh hùng có chạm biên hay không
    boundaryChecking(player)
    # kiểm tra quái vật có chạm biên hay không
    boundaryChecking(goal)
     # kiểm tra va chạm
    if isCollision(player, goal):
        print("Ðã giải cứu được thế giới")
        break
