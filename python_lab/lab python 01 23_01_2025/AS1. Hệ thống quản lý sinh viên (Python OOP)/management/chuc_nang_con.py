
# Cập nhật thông tin sinh viên (hàm này sẽ cập nhật thông tin của sinh viên tìm được)
def cap_nhat_thong_tin(sinh_vien_tim_thay):
    print(f"Thông tin sinh viên {sinh_vien_tim_thay[1]}:")
    print(f"ID: {sinh_vien_tim_thay[0]}, Ngày sinh: {sinh_vien_tim_thay[2]}, Lớp: {sinh_vien_tim_thay[3]}, GPA: {sinh_vien_tim_thay[4]}")
    
    ho_ten_moi = input(f"Nhập họ tên mới cho sinh viên {sinh_vien_tim_thay[1]}: ")
    lop_moi = input(f"Nhập lớp mới cho sinh viên {sinh_vien_tim_thay[1]}: ")
    gpa_moi = input(f"Nhập GPA mới cho sinh viên {sinh_vien_tim_thay[1]}: ")

    sinh_vien_tim_thay[1] = ho_ten_moi if ho_ten_moi else sinh_vien_tim_thay[1]
    sinh_vien_tim_thay[3] = lop_moi if lop_moi else sinh_vien_tim_thay[3]
    try:
        sinh_vien_tim_thay[4] = float(gpa_moi) if gpa_moi else sinh_vien_tim_thay[4]
    except ValueError:
        print("GPA không hợp lệ!")
        return

    print(f"Thông tin đã được cập nhật thành công!")

