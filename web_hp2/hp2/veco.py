import turtle

# Tạo một đối tượng Turtle
flag = turtle.Turtle()

# Đặt màu nền là đỏ (màu đỏ của cờ Việt Nam)
flag.color("red")

# Điều chỉnh kích thước của cửa sổ vẽ
turtle.setup(500, 400)

# Vẽ hình chữ nhật đỏ (nền cờ)
flag.begin_fill()
flag.penup()
flag.goto(-150, 100)
flag.pendown()
flag.forward(200)
flag.right(90)
flag.forward(100)
flag.right(90)
flag.forward(200)
flag.right(90)
flag.forward(100)
flag.end_fill()

# Vẽ sao năm cạnh trên cờ (ngôi sao vàng)
flag.color("yellow")
flag.penup()
flag.goto(-60, 30)
flag.right(15)
flag.pendown()

# Đổ màu bên trong ngôi sao
flag.begin_fill()
for _ in range(5):
    flag.forward(50)
    flag.right(144)   
flag.end_fill()
#đổ màu nốt
flag.color("yellow")
flag.penup()
flag.goto(-54,48)
flag.pendown()
flag.begin_fill()
for _ in range(5):
  flag.forward(12)
  flag.right(75)
flag.end_fill()



# Ẩn con trỏ và hiển thị kết quả
flag.hideturtle()
turtle.done()
