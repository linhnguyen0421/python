print("Hello word")
while True:
  print("Chọn chức năng")
  print("1.Kiểm tra số nguyên tố")
  print("2.Giải phương trình bậc 2")
  print("3.Giải hệ pt bậc 2")
  
  print("*"*50)
  a = input("Chọn ")
  if a == "1":
    n = int(input(">> nhap so tu nhien: "))
    if n <= 1:
      print(n," la so nguyen to") 
    for i in range(2, n):
      if n % i == 0: 
        print(n," khong phai so nguyen to") 
      else:
        print(n," la so nguyen to")      
