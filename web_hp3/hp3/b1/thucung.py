#tạo 1 class có tên là per có các thuộc tính name, species
#name, species, age
class Pet:
    def __init__(self, name, species, age):
        #gán giá trị tham số
        self.name = name #tên
        self.species = species #loai thu cung
        self.age = age #tuoi

    #trả về chuỗi mô tả thông tin của thú cưng
    def describe(self):
        return f"Thú cưng [Tên: {self.name}, Loài: {self.species}, Tuổi: {self.age}]"

    # trả về tiếng kêu
    #lower để chuẩn hóa giá trị của loại(species) vật đó về chữ thường
    def speak(self):
        if self.species.lower() == "chó":
            return "Gâu gâu!"
        elif self.species.lower() == "mèo":
            return "Meo meo!"
        elif self.species.lower() == "chim":
            return "Chíp chíp!"
        else:
            return "..."
 #khai báo 1 lớp để quản lý thú cưng
class PetShop:
    def __init__(self):
        self.pets = [] #ham rong

    def add_pet(self, pet):
        self.pets.append(pet)

    def show_pets(self):
        for pet in self.pets:
            print(pet.describe()) # 
















# Thử nghiệm
pet1 = Pet("Milo", "Chó", 2)
pet2 = Pet("Kitty", "Mèo", 1)
pet3 = Pet("Coco", "Chim", 3)

shop = PetShop()
shop.add_pet(pet1)
shop.add_pet(pet2)
shop.add_pet(pet3)

print("Danh sách thú cưng trong cửa hàng:")
shop.show_pets()

print("\nTiếng kêu của thú cưng:")
for pet in shop.pets:
    print(pet.name,":", pet.speak())
