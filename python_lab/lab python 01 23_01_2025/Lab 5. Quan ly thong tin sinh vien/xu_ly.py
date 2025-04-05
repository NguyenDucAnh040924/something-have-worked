danh_sach_sinh_vien = []  # Danh sách lưu thông tin sinh viên
diem_so = {}  # Dictionary lưu điểm của từng sinh viên

def them_sinh_vien():
    thong_tin_moi_vua_nhap = input("Nhập lần lượt mã số, họ tên và ngày sinh (cách nhau bằng dấu phẩy): ").strip()
    
    # Kiểm tra định dạng đầu vào
    if thong_tin_moi_vua_nhap.count(',') != 2:
        print("Lỗi: Vui lòng nhập đúng định dạng (mã số, họ tên, ngày sinh).")
        return
    
    thong_tin_moi_vua_nhap = thong_tin_moi_vua_nhap.split(',')

    # Loại bỏ khoảng trắng dư thừa
    ma_so = thong_tin_moi_vua_nhap[0].strip()
    ho_ten = thong_tin_moi_vua_nhap[1].strip()
    ngay_sinh = thong_tin_moi_vua_nhap[2].strip()

    # Kiểm tra trùng mã số sinh viên
    if any(sv[0] == ma_so for sv in danh_sach_sinh_vien):
        print(f"Lỗi: Mã số {ma_so} đã tồn tại.")
        return

    # Thêm sinh viên vào danh sách
    sinh_vien = (ma_so, ho_ten, ngay_sinh)
    danh_sach_sinh_vien.append(sinh_vien)

    # Khởi tạo danh sách điểm cho sinh viên mới
    diem_so[ma_so] = []

    print(f"Thêm sinh viên {ho_ten} thành công!")



def them_diem():
    ma_so = input("Nhập mã số sinh viên: ").strip()
    
    if ma_so not in diem_so:
        print("❌ Sinh viên không tồn tại! Vui lòng kiểm tra lại.")
        return

    try:
        diem = float(input("Nhập điểm (0 - 10): ").strip())

        if 0 > diem or diem > 10:
            print("❌ Điểm phải nằm trong khoảng từ 0 đến 10!")
        else:
            diem_so[ma_so].append(diem)  # Thêm điểm hợp lệ vào danh sách
            print(f"✅ Đã thêm điểm {diem} cho sinh viên có mã số {ma_so}.")            
    
    except ValueError:
        print("❌ Lỗi: Điểm phải là số!")


def hien_thi_danh_sach():
    for sinh_vien in danh_sach_sinh_vien:
        ma_so, ho_ten, ngay_sinh = sinh_vien

        print(f"Mã số: {ma_so}")
        print(f"Họ tên: {ho_ten}")
        print(f"Ngày sinh: {ngay_sinh}")

        if ma_so in diem_so:
            print(f"✅ Điểm số: {diem_so[ma_so]}")
        else:
            print("❌ Chưa có điểm")


def tim_kiem_sinh_vien(danh_sach_sinh_vien, danh_sach_diem):
    """
    Tìm kiếm sinh viên theo mã số.
    Hiển thị thông tin chi tiết và điểm số nếu tìm thấy.
    """
    ma_so_can_tim = input("Nhập mã số cần tìm: ").strip()
    
    sinh_vien_tim_thay = None
    for sinh_vien in danh_sach_sinh_vien:
        ma_so, ho_ten, ngay_sinh = sinh_vien
        if ma_so_can_tim.lower() == ma_so.lower():
            sinh_vien_tim_thay = sinh_vien
            break
    
    if sinh_vien_tim_thay:
        ma_so, ho_ten, ngay_sinh = sinh_vien_tim_thay
        print(f"Mã số: {ma_so}\nHọ tên: {ho_ten}\nNgày sinh: {ngay_sinh}")
        
        # Tìm điểm số của sinh viên
        diem_so = danh_sach_diem.get(ma_so, "Không có dữ liệu điểm")
        print(f"Điểm số: {diem_so}")
    else:
        print("Không tìm thấy sinh viên với mã số đã nhập.")


def xoa_sinh_vien(danh_sach_sinh_vien):
    """
    Xóa sinh viên khỏi danh sách theo mã số.
    """
    ma_so_can_xoa = input("Nhập mã số sinh viên cần xóa: ").strip()
    
    for sinh_vien in danh_sach_sinh_vien:
        ma_so, ho_ten, ngay_sinh = sinh_vien
        if ma_so_can_xoa.lower() == ma_so.lower():
            danh_sach_sinh_vien.remove(sinh_vien)
            print(f"Đã xóa sinh viên: {ho_ten}")
            return
    
    print("Không tìm thấy sinh viên để xóa.")



def sap_xep_sinh_vien_theo_ho_ten():
    """
    Sắp xếp danh sách sinh viên theo họ tên theo thứ tự bảng chữ cái.
    """
    danh_sach_sinh_vien.sort(key=lambda sv: sv[1])
    print("Danh sách sinh viên sau khi sắp xếp:")
    for sinh_vien in danh_sach_sinh_vien:
        print(f"Mã số: {sinh_vien[0]}, Họ tên: {sinh_vien[1]}, Ngày sinh: {sinh_vien[2]}") 
            