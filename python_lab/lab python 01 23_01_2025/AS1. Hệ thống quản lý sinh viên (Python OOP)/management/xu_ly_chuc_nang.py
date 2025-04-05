from entity.student import SinhVien
from management.chuc_nang_con import *

# Danh sách sinh viên dưới dạng danh sách con (id, tên, ngày sinh, lớp, GPA)
danh_sach_sinh_vien = [
    ["123", "Nguyen Duc A", "01/01/2000", "CTK42", 3.5],
    ["124", "Nguyen Van B", "02/02/2001", "CTK43", 3.2],
    ["125", "Vu Thanh L", "15/07/1999", "CTK41", 3.8],
    ["126", "Tran Bao N", "20/11/2000", "CTK42", 2.9],
    ["127", "Nguyen Duc A", "10/10/2001", "CTK43", 3.7],
    ["128", "Nguyen Duc A", "05/05/1999", "CTK41", 3.6]
]

# Thêm sinh viên mới vào danh sách
def them_sinh_vien(danh_sach_sinh_vien):
    thong_tin_sinh_vien = input("Nhập thông tin sinh viên cần thêm (id, họ tên, ngày sinh, lớp, GPA): ")

    # Tách thông tin sinh viên thành danh sách các giá trị
    thong_tin_sinh_vien = thong_tin_sinh_vien.split(',')  # Dùng dấu phẩy làm phân tách

    # Kiểm tra độ dài của thông tin nhập vào
    if len(thong_tin_sinh_vien) != 5:
        print("Độ dài không đủ, vui lòng nhập lại thông tin đầy đủ!")
        return

    # Lấy các thông tin sinh viên từ danh sách, cắt bỏ khoảng trắng thừa
    id = thong_tin_sinh_vien[0].strip()
    ho_ten = thong_tin_sinh_vien[1].strip()
    ngay_sinh = thong_tin_sinh_vien[2].strip()
    lop = thong_tin_sinh_vien[3].strip()

    try:
        gpa = float(thong_tin_sinh_vien[4].strip())  # GPA phải là số thực
    except ValueError:
        print("GPA không hợp lệ, vui lòng nhập lại!")
        return

    # Tạo danh sách sinh viên mới và thêm vào danh sách
    sinh_vien_moi = [id, ho_ten, ngay_sinh, lop, gpa]
    danh_sach_sinh_vien.append(sinh_vien_moi)
    print(f"Đã thêm sinh viên: {id} {ho_ten}")

# Tìm kiếm sinh viên trong danh sách
def tim_kiem_sinh_vien(danh_sach_sinh_vien):
    ten_or_id = input("Nhập tên hoặc mã sinh viên: ")
    
    sinh_vien_da_tim_thay = []

    for sinh_vien in danh_sach_sinh_vien:
        if ten_or_id.lower() == sinh_vien[0].lower() or ten_or_id.lower() == sinh_vien[1].lower():
            sinh_vien_da_tim_thay.append(sinh_vien)

    if sinh_vien_da_tim_thay:
        print(f"Đã tìm thấy {len(sinh_vien_da_tim_thay)} sinh viên:")
        for sv in sinh_vien_da_tim_thay:
            print(f"Mã: {sv[0]}, Tên: {sv[1]}, Ngày sinh: {sv[2]}, Lớp: {sv[3]}, GPA: {sv[4]}")
    else:
        print(f"Không tìm được sinh viên nào có tên/id {ten_or_id}! :D")

# Cập nhật thông tin sinh viên
def cap_nhat_thong_tin_sinh_vien(danh_sach_sinh_vien):
    # Kiểm tra danh sách trống
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên đang trống!")
        return

    ten_or_id = input("Nhập tên hoặc ID sinh viên: ").strip()  # Nhập tên hoặc mã sinh viên

    sinh_vien_tim_thay = None

    # Tìm sinh viên trong danh sách
    for tim_kiem in danh_sach_sinh_vien:
        if ten_or_id.lower() == tim_kiem[0].lower() or ten_or_id.lower() == tim_kiem[1].lower():
            sinh_vien_tim_thay = tim_kiem
            break  # Dừng vòng lặp nếu tìm thấy sinh viên

    if sinh_vien_tim_thay:
        cap_nhat_thong_tin(sinh_vien_tim_thay)
    else:
        print(f"Sinh viên {ten_or_id} không tồn tại!")


# Xóa sinh viên khỏi danh sách
def xoa_sinh_vien(danh_sach_sinh_vien):
    pass


# Sắp xếp danh sách sinh viên
def sap_xep_danh_sach(danh_sach_sinh_vien):
    pass


# Lưu danh sách vào file
def luu_danh_sach_sinh_vien(ten_tep, danh_sach_sinh_vien):

    if not danh_sach_sinh_vien:
        print("Danh sách trống! Không thể ghi!")
        return 

    danh_sach_sinh_vien_cu = []
    
    try: 
        with open (ten_tep, 'r') as kiem_tra_file:

            for line in kiem_tra_file:
                sinh_vien_cu = line.strip().split(', ')
                sinh_vien_cu[4] = float(sinh_vien_cu[4])
                danh_sach_sinh_vien_cu.append(sinh_vien_cu)

    except FileNotFoundError:
        danh_sach_sinh_vien_cu = []
    
    
    if danh_sach_sinh_vien_cu != danh_sach_sinh_vien:

        with open (ten_tep, 'a') as ghi_file:

            for sinh_vien in danh_sach_sinh_vien:
                ghi_file.write(', '.join(map(str, sinh_vien)) + '\n')
        print("Danh sách đã được lưu vào file!")
    
    else:
        print("Danh sách không thay đổi, không cần lưu! ")

        



# Đọc danh sách từ file
def doc_danh_sach_sinh_vien(ten_tep):
    

    try:
        with open (ten_tep, 'r') as doc_file:
            if not ten_tep:
                print("File rỗng! ")
                return


            for line in doc_file:
                line = line.strip()
                print(line)

    except FileNotFoundError:
        print(f"File có tên {ten_tep} không tồn tại! ")



















