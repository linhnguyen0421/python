print("******************PHẦN MỀM QUẢN LÝ QUÁN ĂN *****************")
monan = ['Phở Chín', 'Phở Tái', 'Phở Tái Nạm', 'Phở Tái Gầu', 'Phở Đặc Biệt']
gia = [30000, 30000, 35000, 35000, 40000]
# khởi tạo vòng lặp vô hạn để có thể chọn lại các chức năng
while True:
    print("Mời bạn chọn các chức năng sau đây:")
    print("1. Hiển thị danh sách món ăn")
    print("2. Thêm món ăn vào danh sách")
    print("3. Chỉnh sửa thông tin món ăn")
    print("4. Xóa món ăn khỏi danh sách")
    print("5. Gọi món")
    print("6. Thoát chương trình")

    chucNang = int(input("Chọn chức năng: "))

    if chucNang == 1:
        for i in range(len(monan)):
            print(str(i + 1) + ". " + monan[i] + " - " + str(gia[i]) + " VNĐ")
        print("------------------------------")
    elif chucNang == 2:
        #a=input("nhập tên món ăn")
        monan.append(input("Nhập tên món ăn: "))
        gia.append(int(input("Nhập giá: "))) 
        print("Thêm món ăn thành công!")
        print("------------------------------")
    elif chucNang == 3:
        for i in range(len(monan)):
            print(str(i + 1) + ". " + monan[i] + " - " + str(gia[i]) + " VNĐ")
        index = int(input("Chọn số thứ tự món ăn cần chỉnh sửa: "))
        monan[index - 1] = input("Nhập tên món ăn mới: ")
        gia[index - 1] = int(input("Nhập giá mới: "))
        print("Chỉnh sửa thông tin món ăn thành công!")
        print("------------------------------")
    elif chucNang == 4:
        for i in range(len(monan)):
            print(str(i + 1) + ". " + monan[i] + " - " + str(gia[i]) + " VNĐ")
        index = int(input("Chọn số thứ tự món ăn cần xóa: "))
        del monan[index - 1]
        del gia[index - 1]
        print("Xóa món ăn thành công!")
        print("------------------------------")
    elif chucNang == 5:
        danhSachGoiMon = []
        tongTien = 0
        while True:
            print("Danh sách món ăn:")
            for i in range(len(monan)):
                print(str(i + 1) + ". " + monan[i] + " - " + str(gia[i]) + " VNĐ")
            chon = int(input("Chọn món ăn muốn đặt (0 để kết thúc): "))
            if chon == 0:
                break
            print("Chọn số lượng cho món: ",monan[chon - 1])
            soLuong = int(input())
            goimon = [monan[chon - 1],gia[chon - 1],soLuong]
            danhSachGoiMon.append(goimon)
            tongTien += gia[chon - 1] * soLuong
        
        print("-----------------------Hoá Đơn----------------------------")
        print("Danh sách món ăn đã gọi:")
        for i in range(len(danhSachGoiMon)):
            print("-",danhSachGoiMon[i][0],"x",danhSachGoiMon[i][2])
        print("Tổng tiền: " + str(tongTien) + " VNĐ")
        print("---------------------------------------------------------")
    elif chucNang == 6:
        break
    else:
        print("Chức năng không hợp lệ!")
        print("------------------------------")
