class SinhVien:

    def __init__(self, id, ho_ten, ngay_sinh, lop, gpa):
        self.id = id
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.lop = lop
        self.gpa = gpa


    def __init__(self, id, ho_ten):
        self.id = id
        self.ho_ten = ho_ten        


    # Getter cho id
    @property
    def id(self):
        return self._id

    # Setter cho id
    @id.setter
    def id(self, value):
        if value:  # Kiểm tra giá trị hợp lệ, ví dụ không trống
            self._id = value
        else:
            raise ValueError("ID không thể trống")

    # Getter cho ho_ten
    @property
    def ho_ten(self):
        return self._ho_ten

    # Setter cho ho_ten
    @ho_ten.setter
    def ho_ten(self, value):
        if len(value) > 0:
            self._ho_ten = value
        else:
            raise ValueError("Họ tên không thể trống")

    # Getter cho ngay_sinh
    @property
    def ngay_sinh(self):
        return self._ngay_sinh

    # Setter cho ngay_sinh
    @ngay_sinh.setter
    def ngay_sinh(self, value):
        self._ngay_sinh = value  # Bạn có thể thêm kiểm tra định dạng ngày nếu cần

    # Getter cho lop
    @property
    def lop(self):
        return self._lop

    # Setter cho lop
    @lop.setter
    def lop(self, value):
        self._lop = value

    # Getter cho gpa
    @property
    def gpa(self):
        return self._gpa

    # Setter cho gpa
    @gpa.setter
    def gpa(self, value):
        if 0 <= value <= 4:  # Kiểm tra GPA hợp lệ
            self._gpa = value
        else:
            raise ValueError("GPA phải trong khoảng từ 0 đến 4")
    
    def hien_thi_thong_tin(self):
        print(f"ID: {self.id}")
        print(f"Ho ten: {self.ho_ten}")
        print(f"Ngay Sinh: {self.ngay_sinh}")
        print(f"Lop: {self.lop}")
        print(f"GPA: {self.gpa}")
