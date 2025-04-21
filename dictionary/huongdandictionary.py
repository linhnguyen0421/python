# khai bao dictionary
sinhVien={
    "hoVaTen" : "Nguyen Van A",
    "maLop" : "DH01",
    "diemTrungBinh":8.5
}
#in ra dictionary
print(sinhVien)

#in ra ho va ten cuar ban sinh vien, dung ngoac vuong de truy cap keys
print(sinhVien["hoVaTen"])
x= sinhVien["maLop"]

#co the dung get se cho ket qua tuong ung,truyen cho ham get key ma cta can lay
x=sinhVien.get("maLop")
print(x) #(sinhVien.get("maLop"))

#thay doi 1 gia tri
sinhVien["maLop"]="DH02"
sinhVien.update({"maLop":"DH02", "diemTrungBinh":8.6})
print(sinhVien)

#thêm các mục 2 cách them cap key:value
sinhVien["namHoc"]=2025
print(sinhVien)
sinhVien.update({"noiSinh":"TraVinh"})

#loai bo cac muc
sinhVien.pop("noiSinh")
                 #sinhVien.popitem() de xoa du lieu cuoi cung
print(sinhVien)
#or
del sinhVien["noiSinh"]
#del sinhVien #xoa toan bo
# clear() lm trong phuong thuc
sinhVien.clear()
#in tat ca cac khoa trong tu dien, tung cai 1
for x in sinhVien:
    print(x)
#duyet cac gia tri
for x in sinhVien.values():
    print(x)

#duyet cac khoa
for x in sinhVien.keys():
    print(x)

#duyet cac cap khoa- gia tri
for x,y in sinhVien.items():
    print(x,y)
