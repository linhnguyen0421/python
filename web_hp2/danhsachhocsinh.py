#ham tao danh sach luu file
def danhsach():
    f=open("ds.txt",'r')
    data=f.readlines()
    print("DANH SACH HOC SINH")
    for line in data:
        print(line)

    print("------------")
    f.close()
#them hoc vien
def themhocvien():
    f=open("ds.txt","a+")
    print("ban muon them hoc vien:")
    ten=input("nhap ten:")
    tuoi=input("tuoi:")
    lop=input("lop:")
    qq=input("que quan:")
    thongtin=ten+","+tuoi+","+lop+","+qq+"\n"
    f.write(thongtin)
    f.truncate()
    f.close()
    print("ban da them thanh cong")
#xoa hoc sinh
def xoahocsinh():
    stt=int(input("ban muon xoa hoc sinh thu may:"))
    f=open("ds.txt",'r+')
    data=f.readlines()
    f.seek(0)
    #dem so dong
    dem=0
    for line in data:
        if stt !=dem:
            f.write(line)
        dem+=1
    f.truncate()
    f.close()
    print("dan da xoa thanh cong")
#tim kiem
def timkiem():
    ten=input("nhap ten hoc sinh muon tim kiem")
    f=open("ds.txt",'r+')
    data=f.readlines()
    f.seek(0)
    for line in data:
        data2=line.split(",")
        if data2[0]==ten:
            print("thong tin tim kiem duoc la:")
            print(line)
            f.close()
            return
    f.truncate()
    f.close()
 #menu
def menu():
    while True:
        print("-------------MENU-------------")
        print("1.Hien thi danh sach")
        print("2.Them hoc vien")
        print("3.Xoa hoc vien")
        print("4.Tim kiem hoc vien")
        print("5.thoat")
        print("------------------------------")
        choice=int(input("Vui long chon so:"))
        if choice < 1 or choice >5:
            print("xin loi,vui long chon trong khoang 1-5")
        else:
            print("ban lua chon",choice)
            return choice
luachon=True
while luachon:
    choice = menu()
    if choice==1:
        danhsach()
    if choice==2:
        themhocvien()
    if choice==3:
        xoahocsinh()
    if choice==4:
        timkiem()
    if choice==5:
        luachon=False
