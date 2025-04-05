from phan_tich_email import *
import json

menuList = ["Thống kê email theo người gửi", "Tiềm kiếm email theo tiêu đề hoặc nội dung",
            "Đếm số lần xuất hiện của một ký tự", "Đếm số lượng từ trong email",
            "Thay thế nội dung", "Lưu kết quá thống kê", "Thoát"]

danh_sach_email = doc_email("hoc_tap_email.txt")

while True:

    j = 0
    for i in menuList:
        j += 1
        print(f"{j}. {i}")


    lua_chon = int(input("Nhập lựa chọn của bạn: "))
    print("---------------------------------------------------------------")

    match lua_chon:
        case 1:
            thong_ke = thong_ke_nguoi_gui(danh_sach_email)
            # print(f"{thong_ke=}")
            for nguoi_gui in thong_ke:
                print(f"{nguoi_gui} : {thong_ke[nguoi_gui]}")
            print()
        case 2:
            tu_khoa = input("Nhập từ khóa của bạn: ")
            ket_qua = tim_kiem_email(danh_sach_email, tu_khoa)
            for line in ket_qua: 
                email = line
            # print(f"{ket_qua=}")
            print(json.dumps(email,indent=4, ensure_ascii=False))
        case 3: 
            ky_tu = input("Nhập ký tự cần đếm: ")
            so_lan = dem_ky_tu(ky_tu)
            print(f"Số lần xuất hiện của {ky_tu}: {so_lan}")
        case 4: 
            input_ = input("Nhập tiêu đề or thứ tự mail: ")
            if int(input_) >= 1 and int(input_)  < len(danh_sach_email)+1:
                so_luong_tu = dem_tu(int(input_) , danh_sach_email)
            else:
                so_luong_tu = dem_tu(str(input_), danh_sach_email)
            
            print(f"{so_luong_tu= }")
        case 5: 
            thutu = 0
            for thuTu in danh_sach_email:
                thutu += 1
                print(f" so thu tu= {thutu}. tieu de= {thuTu['nguoi_gui']}, thu tu= {thuTu['tieu_de']}")

            input_ = input("Nhập tiêu đề or thứ tự mail: ")
            chuoi_cu = input("Nhập chuỗi cũ: ")
            chuoi_moi = input("Nhập chuỗi mới: ")
            if int(input_) >= 1 and int(input_) < len(danh_sach_email)+1:
                thay_the_noi_dung(int(input_), danh_sach_email, chuoi_cu, chuoi_moi)
            else:
                thay_the_noi_dung(str(input_), danh_sach_email, chuoi_cu, chuoi_moi)
            
        case 6: 
            tep_moi = input("Nhập tên tệp muốn lưu: ")
            luu_ket_qua_thong_ke(tep_moi,danh_sach_email)

        case 7: 
            print("Thoát chương trình thành công!")
            break
        
        case _ : 
            print("Lựa chọn không hợp lệ!")