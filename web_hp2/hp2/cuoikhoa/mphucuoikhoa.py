import turtle
import time
import random
t=turtle.Turtle()
turtle.bgcolor("white")
   
# Vẽ hình tròn
def vehinhtron():
    t.penup()
    t.goto(0, -125)
    t.pendown()
    t.circle(125)
# Phân cách phần của hình tròn
def phanchiaphan():
  for i in range(5):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(72)
    t.forward(125)
t.shape("arrow")  # Thiết lập hình dạng là "arrow" (mũi tên)
# Random tốc độ
tocdo = random.randint(35,100)
# Định nghĩa hàm để xoay đối tượng Turtle ngẫu nhiên theo thời gian
def xoay_ngau_nhien(thoi_gian,speed):
    t.goto(0,0)
    thoi_gian_bat_dau = time.time()
    while time.time() - thoi_gian_bat_dau < thoi_gian:
        t.left(speed)
        time.sleep(0.1)  # Đợi 0.1 giây giữa các bước xoay
nguoichoi1 = input("Nhập tên người chơi 1:")
nguoichoi2 = input("Nhập tên người chơi 2:")
nguoichoi3 = input("Nhập tên người chơi 3:")
nguoichoi4 = input("Nhập tên người chơi 4:")
nguoichoi5 = input("Nhập tên người chơi 5:")
def nguoichoi():
   t.penup()
   t.goto(-100,0)
   t.write(nguoichoi1, font=("Arial", 10, "normal"))
   t.penup()
   t.goto(-45,70)
   t.write(nguoichoi2, font=("Arial", 10, "normal"))
   t.penup()
   t.goto(40,40)
   t.write(nguoichoi3, font=("Arial", 10, "normal"))
   t.penup
   t.goto(30,-60)
   t.write(nguoichoi4, font=("Arial", 10, "normal"))
   t.penup
   t.goto(-55,-70)
   t.write(nguoichoi5, font=("Arial", 10, "normal"))
vehinhtron()
phanchiaphan()
nguoichoi()
xoay_ngau_nhien(3,tocdo)
turtle.done()
