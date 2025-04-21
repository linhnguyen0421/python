[]
# list
()
#touple
# dictionary
# dict ( viết tắt)
# Có chức năng lưu trữ các giá trị chứ KEY và VALUE và các dữ liệu này không đc sắp xếp 
#  theo 1 thứ tự nào cả 


# 1 : là được bọc trong dấu ngoặc nhọn '{}' và tất cả những gì có trong ngoặc nhọn nó là phần tử ','
#2 các phần tử của nó phải là 1 cặp đi với nhau theo kiểu KEY-value 
# 3 Các key trong dict đc ngăn cách bởi dấu : 

# Key = chìa khóa ( nó là duy nhất và không thể thay đổi key thường là 1 chuỗi, 1 số ,  1 touple )
# Value = giá trị ( Có thể là 1 giá trị bất kì, có thể thay đổi được, có thể thêm/ sửa / xóa)
################################
#Cách khởi tạo 1 Dict 
hocSinh ={
    'name1':'Nguyễn Đức Nam',
    'age':21,
    'number':'7',
    '10':'Day la số 10',
    'name2':'Nguyễn Đức Hà',
    1:'14'
    }
# print(hocSinh['name1'])
# # thêm 1 phần tử vào list
# hocSinh['que quan']='Bắc Ninh'
# print(hocSinh)
# del hocSinh['name2']
# print(hocSinh)

#  Hãy in tất cả các key của dict hocSinh
# c1
# print(hocSinh.keys())

# c2 
# for key in hocSinh:
#     print(key)

# bài 2 Cho trước dict hocsinh, hãy nhập key sau đó thì kiểm tra xem có trong dict khôgn, nếu có --> kết thúc trương chình
# nêú không thì yêu cầu nhập vào giá trị ->thêm giá trị và kety vừa nhập

key =input()
if key not in hocSinh:
    value=input()
    hocSinh[key]=value
print(hocSinh)
