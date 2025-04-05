from xu_ly_file import *

# --------------- CT chính --------------
menuList = ["Hiển thị danh sách sinh viên","Thêm sinh viên mới","Cập nhật điểm",
            "Xóa sinh viên","Tìm kiếm sinh viên","Sắp xếp danh sách","Thống kê","Thoát"]


while True:
    j = 0
    for i in menuList:
        j += 1
        print(f"{j}. {i}")

    lua_chon_menu = int(input("Chọn mục: "))

    # Xử lý lựa chọn
    if lua_chon_menu == 1:
        hien_thi_danh_sach()
    elif lua_chon_menu == 2:
        them_sinh_vien()
    elif lua_chon_menu == 3: 
        cap_nhat_diem()
    elif lua_chon_menu == 4:
        xoa_sinh_vien()
    elif lua_chon_menu == 5:
        tim_kiem_sinh_vien()
    elif lua_chon_menu == 6:
        sap_xep_danh_sach()
    elif lua_chon_menu == 7:
        thong_ke()
    elif lua_chon_menu == 8:
        break
    else: 
        print("Lựa chọn không hợp lệ! Mời nhập lại")
        