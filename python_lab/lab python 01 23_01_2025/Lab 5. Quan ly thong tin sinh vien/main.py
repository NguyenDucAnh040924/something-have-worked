from xu_ly import *

# --------------- CT chính --------------
menuList = ["Thêm sinh viên", "Thêm điểm", "Hiển thị danh sách sinh viên",
            "Tìm kiếm sinh viên", "xóa sinh viên", "Sắp xếp danh sách", "Thoát"]


while True:
    print("----------- MENU -------------------")
    j = 0
    for i in menuList:
        j += 1
        print(f"{j}. {i}")

    lua_chon_menu = int(input("Chọn mục: "))

    # Xử lý lựa chọn
    if lua_chon_menu == 1:
        them_sinh_vien()
    elif lua_chon_menu == 2:
        them_diem()
    elif lua_chon_menu == 3: 
        hien_thi_danh_sach()
    elif lua_chon_menu == 4:
        tim_kiem_sinh_vien()
    elif lua_chon_menu == 5:
        xoa_sinh_vien()
    elif lua_chon_menu == 6:
        sap_xep_sinh_vien_theo_ho_ten()
    elif lua_chon_menu == 7:
        break
    else: 
        print("Lựa chọn không hợp lệ! Mời nhập lại")
        