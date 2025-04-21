#các khai báo lớp khách hàng
class Khach_hang:
    name="SY MINH"
    age=35
    male=True
    money=1
    phone=1234   
    #phuong thuc
    #setter dùng để gán giá trị cho thuộc tính name
    def setName(self,name):
        self.name=name

    #getter dùng để truy xuất giá trị của thuộc tính name
    def getName(self):
        return self.name
    
#khai bao Object là lớp khách hàng
kh=Khach_hang()

#in ra các thuộc tính trong lớp class
print(kh.name)
print(kh.age)
print(kh.male)
print(kh.money)
print(kh.phone)

#gán gtri cho tên và truy xuất tên bằng phương thức setter và getter
kh.setName("Nguyen Thi Anh")
print(kh.getName())

