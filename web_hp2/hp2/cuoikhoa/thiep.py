import turtle

# Function to draw a petal
def draw_petal(turtle, radius):
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)

# Draw flower
def draw_flower():
    flower = turtle.Turtle()
    flower.begin_fill()
    flower.speed(10)
    flower.color("orange")

    for _ in range(6):
        draw_petal(flower, 100)
        flower.left(60)
    flower.end_fill()

# Draw leaves
def draw_leaf():
    leaf = turtle.Turtle()
    leaf.begin_fill()
    leaf.penup()
    leaf.goto(-105, 3)
    leaf.pendown()
    leaf.color("light green")
    leaf.circle(25)
    leaf.left(120)
    leaf.circle(25)
    leaf.left(120)
    leaf.circle(25)
    leaf.end_fill()

    leaf.begin_fill()
    leaf.penup()
    leaf.goto(-35, 50)
    leaf.pendown()
    leaf.color("green")
    leaf.circle(10)
    leaf.left(120)
    leaf.circle(10)
    leaf.left(120)
    leaf.circle(10)
    leaf.end_fill()

# Function to draw a balloon
def draw_balloon():
    balloon = turtle.Turtle()
    balloon.begin_fill()
    balloon.color("red")
    balloon.penup()
    balloon.goto(225, 20)
    balloon.pendown()
    balloon.circle(50)
    balloon.end_fill()

# in thiệp
def print_invitation(teacher_name):
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.write(f"Dear {teacher_name},", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(-100, -70)
    turtle.pendown()
    turtle.write("Chúc thầy/cô một ngày nhà giáo thật ý nghĩa.", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(-100, -90)
    turtle.pendown()
    turtle.write("our Teacher's Day Celebration!", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(-100, -110)
    turtle.pendown()
    turtle.write("Thời gian: thứ 2 ngày 20 tháng 11  năm 2023", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(-100, -130)
    turtle.pendown()
    turtle.write("Thời gian: 15:00 ", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(-100, -150)
    turtle.pendown()
    turtle.write("Địa điểm: Teky Mỹ Đình", font=("Arial", 12, "normal"))

# nhập tên giáo viên
teacher_name = input("Nhập tên giáo viên bạn muốn mời: ")

# Draw the flower, leaves, and balloon
draw_flower()
draw_leaf()
draw_balloon()

# Print the invitation with the entered teacher's name
print_invitation(teacher_name)

turtle.done()
