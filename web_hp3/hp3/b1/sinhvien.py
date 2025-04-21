#Tạo ra 1 lớp sinh viên có các thuộc tính hoTen, queQuan, lop, diemToan, diemVan
class SinhVien:
    def __init__(self, hoTen, queQuan, lop, diemToan, diemVan):
        self.hoTen = hoTen  # truy cập các thuộc tính của đối tượng
        self.queQuan = queQuan
        self.lop = lop
        self.diemToan = diemToan
        self.diemVan = diemVan
# tạo hàm tính điểm trung bình của diemToan và diemVan
    def tinhDiemTB(self):
        dtb = (self.diemToan + self.diemVan) / 2
        return round(dtb, 2) # hàm làm tròn giá trị đến so thập phân thứ 2
# tạo hàm xếp loại học sinh xuất sắc, giỏi, khá, tb, yếu dùng if elif else
    def xepLoai(self, dtb):
# tạo hàm hiển thị thông tin bao gồm dtb, xếp loại, họ tên, quê quán, lớp, điểm toán, điểm văn
        if dtb < 5:
            return "Yếu"
        elif 5 <= dtb < 7:
            return "Trung bình"
        elif 7 <= dtb < 8:
            return "Khá"
        elif 8 <= dtb < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"
    def hienThiThongTin(self):
        # Tính điểm trung bình
        dtb = self.tinhDiemTB()
        # Lấy xếp loại
        xepLoai = self.xepLoai(dtb)
        # Hiển thị thông tin
        print("Họ tên:", self.hoTen)
        print("Quê quán:", self.queQuan)
        print("Lớp:", self.lop)
        print("Điểm Toán:", self.diemToan)
        print("Điểm Văn:", self.diemVan)
        print("Điểm trung bình:", dtb)
        print("Xếp loại:", xepLoai)

# Tạo một đối tượng SinhVien
sv = SinhVien("Nguyen Van A", "Ha Noi", "10A1", 8.5, 7.2)
sv.hienThiThongTin()
