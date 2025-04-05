from management.xu_ly_chuc_nang import *

#  ------------------- CT chính -----------------------------


menuList = ["Hiển thị thông tin tất cả sinh viên", "Tìm kiếm sinh viên theo ID hoặc họ tên",
            "Cập nhật thông tin sinh viên", "Xóa sinh viên khỏi danh sách", "Sắp xếp danh sách sinh viên",
            "Lưu danh sách vào file","Đọc danh sách từ file"]

key_exit = ["8","clear"]

while True:
    index = 0
    for menu in menuList:
        index += 1
        print(f"{index}. {menu}")

    
    print("==============================================")

    lua_chon = input("Nhập lựa chọn: ")
    match lua_chon:
        case '1':
            pass
        case '2':
            pass
        case '3': 
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            ten_tep = "testFD.txt"
            luu_danh_sach_sinh_vien(ten_tep,danh_sach_sinh_vien)
        case '7':
            ten_tep = "testFD.txt"
            doc_danh_sach_sinh_vien(ten_tep)
        case _ if lua_chon in key_exit:
            print("Thoát CT thành công")
            break
        case _:
            print(f"Giá trị {lua_chon} không hợp lệ! ")