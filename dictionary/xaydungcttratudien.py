tuDien={} #khai bao tu dien

while(True):
    print("vui long lua chon chuc nang (bang so): ");
    print("""    1.Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển
    2.Tra cứu ý nghĩa của 1 từ mới 
    3.Cho phép người dùng xóa đi 1 từ vựng trong từ điển
    4.Cho phép người dùng xóa toàn bộ từ điển
    5.Cho phép người dùng in ra toàn bộ từ vựng
    6.Cho phép người dùng in ra toàn bộ từ vựng theo cấu trúc: “TỪ VỰNG” : “Ý NGHĨA”
    7.Kết thúc chương trình
    """)
    luaChon=int(input("Nhap vao lua chon cua ban : "))
    if(luaChon == 1):
        tuVung=input("Nhap vao tu vung : ")
        yNghia=input("Nhap vao y nghia : ")
        tuDien[tuVung]= yNghia
        print("Da them tu vung thanh cong")
    elif(luaChon ==2):
        tuVung=input("Nhap vao tu can tra: ")
        print("Y nghia: ",tuDien[tuVung])
    elif(luaChon ==3):
        tuVung=input("Nhap vao tu can xoa: ")
        tuDien.pop(tuVung)
        print("Da xoa du lieu")
        
    elif(luaChon ==4):
        tuDien.clear()
        print("Da xoa toan bo du lieu")
        
    elif(luaChon ==5):
        print("Hien thi toan bo tu dien")
        for x in tuDien.keys():
            print(x)
            
    elif(luaChon ==6):
        print("Danh sach cac tu vung co trong tu dien: " )
        for x,y in tuDien.items():
            print(x, ":",y )
    elif(luaChon ==7):
         break
    else:
        print("Nhap lua chon khong dung, vui long nhập ")
