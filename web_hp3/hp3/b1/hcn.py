#khai báo hình chữ nhật có sẵn thuộc tính
# class hcn:
#     dai=3
#     rong=4
#     def dientich(self,dai,rong):
#         self.dai=dai
#         self.rong=rong
#         return self.dai*self.rong # in kết quả
# hcn1=hcn() #khai báo 1 đối tượng
# hcn1.dientich(3,4)
# print("CD =",hcn1.dai)
# print("CR =",hcn1.rong)
# print("S =",hcn1.dientich(3,4))

#khai báo hình chữ nhật cần nhập vào thuộc tính
class hcn:
    def dientich(self,dai,rong):
        self.dai=dai
        self.rong=rong
        return self.dai*self.rong
while(True):
    dai=int(input("cd= "))
    if(0<=dai<=10):
        print(dai)
        break
    else:
        print("vui long nhap lai")
rong = float(input("Nhập chiều rộng: "))
hcn1=hcn()
#hcn1.dientich(dai,rong)
print("CD =",hcn1.dai)
print("CR =",hcn1.rong)
print("S =",hcn1.dientich(dai,rong))

#baitap
#1.tính chu vi hình chữ nhật
#2.kiểm tra xem hình đó có phải hình vuông không





class Rectangle:
    #hàm khởi tạo
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def dientich(self):
        return self.length * self.width

    def chuvi(self):
        return 2 * (self.length + self.width)

    def hv(self):
        return self.length == self.width

    def display_info(self):
        print(f"Chiều dài: {self.length}")
        print(f"Chiều rộng: {self.width}")
        print(f"Diện tích: {self.dientich()}")
        print(f"Chu vi: {self.chuvi()}")
        if self.hv():
            print("Đây là hình vuông.")
        else:
            print("Đây là hình chữ nhật.")


# Nhập chiều dài và chiều rộng từ người dùng
length = float(input("Nhập chiều dài: "))
width = float(input("Nhập chiều rộng: "))

# Tạo đối tượng Rectangle
rectangle = Rectangle(length, width)


