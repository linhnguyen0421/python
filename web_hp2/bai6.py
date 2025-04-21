#chèn thư v
import turtle

#khơi tạo màn hình đồ họa 
k=turtle.Screen()

# thiết lập màu nền mau xam
k.bgcolor('gray')

#khoi tao doi tuong do hoa
t=turtle.Turtle()

#cac hinh dang
t.shape('turtle')
def c1():
    t.penup()#nhac but
    t.goto(-165,0)
    t.pendown()#dat but
    t.width(5)# do day cua but
    t.color("blue")# mau but
    t.circle(75)# kich thuoc hinh tron, ban kinh

def c2():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.width(5)
    t.color("black")
    t.circle(75)
def c3():
    t.penup()
    t.goto(165,0)
    t.pendown()
    t.width(5)
    t.color("red")
    t.circle(75)
def c4():
    t.penup()
    t.goto(-85,-85)
    t.pendown()
    t.width(5)
    t.color("yellow")
    t.circle(75)
def c5():
    t.penup()
    t.goto(85,-85)
    t.pendown()
    t.width(5)
    t.color("green")
    t.circle(75)
c1()
c2()
c3()
c4()
c5()
