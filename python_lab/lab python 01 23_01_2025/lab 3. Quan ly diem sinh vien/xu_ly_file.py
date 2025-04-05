def hien_thi_danh_sach():

    # Mở tệp để đọc 
    with open('diem_sinh_vien.txt') as file:
        
        # print(file.read())

        # Đọc từng dòng trong tệptệp
        for line in file:
            # Tách thông tin sinh viênviên
            thong_tin = line.strip().split(",")
            ma_so = thong_tin[0]
            ho_ten = thong_tin[1]
            diem = thong_tin[2]

            # Hiển thị thông tin
            print(ma_so, ho_ten, diem)
    print("Hiển thị danh sách thành công!")
        


def them_sinh_vien():
    try:
        # Nhập thông tin sinh viên mới
        thong_tin_vua_nhap = input("Nhập lần lượt mã số, họ tên và điểm (cách nhau bởi dấu ','): ")
        thong_tin_vua_nhap = thong_tin_vua_nhap.strip().split(',')

        # Kiểm tra xem nhập đúng đủ 3 phần không
        if len(thong_tin_vua_nhap) != 3:
            print("Lỗi: Bạn phải nhập đúng 3 thông tin (mã số, họ tên, điểm)!")
            return

        ma_so_moi, ho_ten_moi, diem_moi = thong_tin_vua_nhap

        # Kiểm tra điểm có hợp lệ không (phải là số)
        try:
            diem_moi = float(diem_moi)  # Chuyển điểm sang số thực để kiểm tra
            if diem_moi < 0 or diem_moi > 10:
                print("Lỗi: Điểm phải từ 0 đến 10!")
                return
        except ValueError:
            print("Lỗi: Điểm phải là một số hợp lệ!")
            return

        # Mở file ở chế độ 'a' để ghi tiếp mà không xóa dữ liệu cũ
        with open('diem_sinh_vien.txt', 'a', encoding='utf-8') as ghi_du_lieu:
            ghi_du_lieu.write(f"\n{ma_so_moi},{ho_ten_moi},{diem_moi}\n")

        print("Thêm sinh viên thành công!")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")


def cap_nhat_diem():
    try:
        # Nhập thông tin cần cập nhật
        thong_tin_vua_nhap = input("Nhập mã số sinh viên và điểm mới (cách nhau bởi dấu ','): ")
        thong_tin_vua_nhap = thong_tin_vua_nhap.strip().split(',')

        # Kiểm tra định dạng dữ liệu đầu vào
        if len(thong_tin_vua_nhap) != 2:
            print("Lỗi: Bạn phải nhập đúng 2 thông tin (mã số, điểm mới)!")
            return

        ma_so_moi, diem_moi = thong_tin_vua_nhap

        # Kiểm tra điểm hợp lệ
        try:
            diem_moi = float(diem_moi)  # Chuyển thành số thực để kiểm tra
            if diem_moi < 0 or diem_moi > 10:
                print("Lỗi: Điểm phải từ 0 đến 10!")
                return
        except ValueError:
            print("Lỗi: Điểm phải là một số hợp lệ!")
            return

        danh_sach_moi = []
        cap_nhat_thanh_cong = False

        # Đọc dữ liệu từ file và cập nhật điểm
        with open('diem_sinh_vien.txt', 'r', encoding='utf-8') as file:
            for line in file:
                thong_tin = line.strip().split(',')
                if thong_tin[0] == ma_so_moi:
                    # Cập nhật điểm mới
                    line = f"{thong_tin[0]},{thong_tin[1]},{diem_moi}\n"
                    cap_nhat_thanh_cong = True
                danh_sach_moi.append(line)

        # Nếu không tìm thấy sinh viên, thông báo lỗi
        if not cap_nhat_thanh_cong:
            print(f"Lỗi: Không tìm thấy sinh viên có mã số {ma_so_moi}!")
            return

        # Ghi danh sách mới vào file (ghi đè toàn bộ nội dung)
        with open('diem_sinh_vien.txt', 'w', encoding='utf-8') as file:
            file.writelines(danh_sach_moi)

        print("Cập nhật điểm thành công!")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")






def xoa_sinh_vien():
    # Nhập mã số sinh viên cần xóa
    ma_so_can_xoa = input("Nhập mã số sinh viên cần xóa: ").strip()

    # Đọc danh sách sinh viên từ file
    with open('diem_sinh_vien.txt', 'r', encoding='utf-8') as file:
        danh_sach_sinh_vien = file.readlines()

    # Xóa sinh viên nếu tìm thấy
    danh_sach_moi = []
    sinh_vien_ton_tai = False

    for line in danh_sach_sinh_vien:
        thong_tin = line.strip().split(',')
        if thong_tin[0] == ma_so_can_xoa:
            sinh_vien_ton_tai = True
            continue  # Bỏ qua dòng này để xóa sinh viên
        danh_sach_moi.append(line)

    # Kiểm tra nếu không tìm thấy sinh viên
    if not sinh_vien_ton_tai:
        print(f"Lỗi: Không tìm thấy sinh viên có mã số {ma_so_can_xoa}!")
        return

    # Ghi danh sách mới vào file (ghi đè nội dung)
    with open('diem_sinh_vien.txt', 'w', encoding='utf-8') as file:
        file.writelines(danh_sach_moi)

    print("Xóa sinh viên thành công!")




def tim_kiem_sinh_vien():
    # Nhập mã số sinh viên hoặc họ tên
    ma_so_OR_ho_ten = input("Nhập mã số hoặc họ tên: ").strip()

    # Đọc danh sách sinh viên từ file
    with open('diem_sinh_vien.txt', 'r', encoding='utf-8') as file:
        danh_sach_sinh_vien = file.readlines()

    # Danh sách chứa kết quả tìm kiếm
    danh_sach_tim_kiem = []
    
    for line in danh_sach_sinh_vien:
        thong_tin = line.strip().split(',')
        
        # Kiểm tra tìm kiếm theo mã số sinh viên
        if thong_tin[0].lower() == ma_so_OR_ho_ten.lower():
            danh_sach_tim_kiem.append(line)
        
        # Kiểm tra tìm kiếm theo họ tên (so khớp một phần)
        elif ma_so_OR_ho_ten.lower() in thong_tin[1].lower():
            danh_sach_tim_kiem.append(line)

    # Kiểm tra kết quả tìm kiếm
    if not danh_sach_tim_kiem:
        print(f"Lỗi: Không tìm thấy sinh viên có thông tin '{ma_so_OR_ho_ten}'!")
    else:
        print("Kết quả tìm kiếm:")
        for sv in danh_sach_tim_kiem:
            print(sv.strip())


def sap_xep_danh_sach():
    try:
        # Đọc danh sách sinh viên từ file
        with open('diem_sinh_vien.txt', 'r', encoding='utf-8') as file:
            danh_sach_sinh_vien = file.readlines()
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'diem_sinh_vien.txt'!")
        return

    danh_sach_sinh_vien_sach = []  # Danh sách đã làm sạch

    for line in danh_sach_sinh_vien:
        thong_tin = [x.strip() for x in line.strip().split(',')]  # Xóa khoảng trắng thừa

        # Kiểm tra dữ liệu hợp lệ (đủ 3 phần tử)
        if len(thong_tin) < 3:
            continue  # Bỏ qua dòng không hợp lệ

        try:
            thong_tin[2] = float(thong_tin[2])  # Chuyển điểm sang số thực
            danh_sach_sinh_vien_sach.append(thong_tin)
        except ValueError:
            print(f"Lỗi: Điểm không hợp lệ trong dòng '{line.strip()}'!")

    # Sắp xếp danh sách theo điểm tăng dần
    danh_sach_sinh_vien_sach.sort(key=lambda x: x[2])

    # Ghi danh sách đã sắp xếp vào file mới
    with open('diem_sinh_vien.txt', 'w', encoding='utf-8') as file:
        for sv in danh_sach_sinh_vien_sach:
            file.write(f"{sv[0]}, {sv[1]}, {sv[2]:.1f}\n")

    print("Đã sắp xếp danh sách theo điểm và lưu vào 'diem_sinh_vien_sap_xep.txt'.")





def thong_ke():
    try:
        # Đọc danh sách sinh viên từ file
        with open('diem_sinh_vien.txt', 'r', encoding='utf-8') as file:
            danh_sach_sinh_vien = file.readlines()
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'diem_sinh_vien.txt'!")
        return

    dem_diem_tren_tb = 0
    tong_diem_tb = 0.0
    sinh_vien_diem_cao_nhat = None
    sinh_vien_diem_thap_nhat = None
    diem_cao_nhat = float('-inf')  # Khởi tạo với giá trị rất nhỏ
    diem_thap_nhat = float('inf')  # Khởi tạo với giá trị rất lớn

    for line in danh_sach_sinh_vien:
        thong_tin = [x.strip() for x in line.strip().split(',')]  # Xóa khoảng trắng thừa

        # Kiểm tra dữ liệu hợp lệ (phải có ít nhất 3 phần tử)
        if len(thong_tin) < 3:
            continue  # Bỏ qua dòng không hợp lệ

        try:
            diem = float(thong_tin[2])  # Chuyển điểm sang số thực
            tong_diem_tb += diem

            # Kiểm tra điểm trên trung bình
            if diem > 5.0:
                dem_diem_tren_tb += 1

            # Tìm sinh viên có điểm cao nhất
            if diem > diem_cao_nhat:
                diem_cao_nhat = diem
                sinh_vien_diem_cao_nhat = thong_tin

            # Tìm sinh viên có điểm thấp nhất
            if diem < diem_thap_nhat:
                diem_thap_nhat = diem
                sinh_vien_diem_thap_nhat = thong_tin

        except ValueError:
            print(f"Lỗi: Điểm không hợp lệ trong dòng '{line.strip()}'!")

    # Tính điểm trung bình nếu có sinh viên hợp lệ
    if len(danh_sach_sinh_vien) > 0 and dem_diem_tren_tb > 0:
        diem_tb_chung = tong_diem_tb / len(danh_sach_sinh_vien)
        print("Điểm trung bình của tất cả sinh viên là: {:.2f}".format(diem_tb_chung))
    else:
        print("Không có dữ liệu hợp lệ để tính điểm trung bình!")

    # Hiển thị sinh viên có điểm cao nhất và thấp nhất nếu có
    if sinh_vien_diem_cao_nhat:
        print(f"Sinh viên có điểm cao nhất: {', '.join(sinh_vien_diem_cao_nhat)}")
    if sinh_vien_diem_thap_nhat:
        print(f"Sinh viên có điểm thấp nhất: {', '.join(sinh_vien_diem_thap_nhat)}")

    print("Số lượng sinh viên có điểm trên trung bình là:", dem_diem_tren_tb)

