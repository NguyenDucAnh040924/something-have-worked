import json

def doc_email(ten_tep):
    danh_sach_email = []

    with open (ten_tep, 'r') as file_only_read:
        email = {}

        for line in file_only_read:
            if line.startswith("From:"):
                if email: # Nếu email có data
                    danh_sach_email.append(email)
                    email = {} # Reset cho mail mới
                email["nguoi_gui"] = line.split(":")[1].strip()
            
            elif line.startswith("To:"):
                email["nguoi_nhan"] = line.split(":")[1].strip()

            elif line.startswith("Sent:"):
                email["thoi_gian"] = line.split(":")[1].strip()

            elif line.startswith("Subject:"):
                email["tieu_de"] = line.split(":")[1].strip()

            elif line != "\n":
                if "noi_dung" not  in email:
                    email["noi_dung"] = ""
                email["noi_dung"] += line + "\n"

        if email: # Thêm email cuối cùng vào danh sách
            danh_sach_email.append(email)

        file_only_read.close()

        return danh_sach_email

def thong_ke_nguoi_gui(danh_sach_email):
    thong_ke = {}
    for email in danh_sach_email:
        nguoi_gui = email["nguoi_gui"]
        if nguoi_gui in thong_ke:
            thong_ke[nguoi_gui] += 1
        else:
            thong_ke[nguoi_gui] = 1

    return thong_ke


def tim_kiem_email(danh_sach_email, tu_khoa):
    ket_qua = []
    for email in danh_sach_email:

        tieu_de = email["tieu_de"].lower()
        noi_dung = email["noi_dung"].lower()
        tu_khoa = tu_khoa.lower()     

        if (tu_khoa in tieu_de
            or tu_khoa in noi_dung):
            
            ket_qua.append(email)
    
    return ket_qua


def dem_ky_tu(danh_sach_email, ky_tu):
    tong_so_lan = 0

    for email in danh_sach_email:
        tong_so_lan += email["noi_dung"].count(ky_tu)
    
    return tong_so_lan


def dem_tu(tieu_de_email_OR_thu_tu_mail, danh_sach_email):
    # Kiểm tra nếu danh sách email rỗng
    if not danh_sach_email:
        print("Danh sách email trống.")
        return None

    email = None
    
    # Kiểm tra nếu người dùng nhập số thứ tự email
    if isinstance(tieu_de_email_OR_thu_tu_mail, int):
        if 1 <= tieu_de_email_OR_thu_tu_mail < len(danh_sach_email)+1:
            email = danh_sach_email[tieu_de_email_OR_thu_tu_mail-1]
        else:
            print("Số thứ tự email không hợp lệ.")
            return None
    # Nếu người dùng nhập tiêu đề email
    elif isinstance(tieu_de_email_OR_thu_tu_mail, str):
        email = next((e for e in danh_sach_email if e.get("tieu_de") == tieu_de_email_OR_thu_tu_mail), None)
        if email is None:
            print("Không tìm thấy email có tiêu đề này.")
            return None
    else:
        print("Định dạng nhập vào không hợp lệ.")
        return None

    # Kiểm tra xem email có nội dung không
    noi_dung = email.get("noi_dung", "")
    danh_sach_tu = noi_dung.split()
    so_luong_tu = len(danh_sach_tu)

    return so_luong_tu



def thay_the_noi_dung(tieu_de_email_OR_thu_tu_mail, danh_sach_email, chuoi_cu, chuoi_moi):
    """
    ○ Cho phép người dùng chọn một email (bằng cách nhập số thứ tự hoặc tiêu đề).
    ○ Cho phép người dùng nhập vào hai chuỗi: chuỗi cần thay thế và chuỗi thay thế.
    ○ Thay thế tất cả các lần xuất hiện của chuỗi cần thay thế bằng chuỗi thay thế trong nội dung email.
    ○ Hiển thị nội dung email sau khi thay thế.
    """

    # Kiểm tra nếu danh sách email rỗng
    if not danh_sach_email:
        print("Danh sách email trống.")
        return

    email = None

    # Kiểm tra nếu người dùng nhập số thứ tự email
    if isinstance(tieu_de_email_OR_thu_tu_mail, int):
        if 1 <= tieu_de_email_OR_thu_tu_mail <= len(danh_sach_email):
            email = danh_sach_email[tieu_de_email_OR_thu_tu_mail - 1]  # Chỉnh index về đúng vị trí
        else:
            print("Số thứ tự email không hợp lệ.")
            return

    # Nếu người dùng nhập tiêu đề email
    elif isinstance(tieu_de_email_OR_thu_tu_mail, str):
        email = next((e for e in danh_sach_email if e["tieu_de"] == tieu_de_email_OR_thu_tu_mail), None)
        if email is None:
            print("Không tìm thấy email có tiêu đề này.")
            return

    else:
        print("Định dạng nhập vào không hợp lệ.")
        return

    # Thực hiện thay thế nội dung
    noi_dung_mail_cu = email["noi_dung"]
    email["noi_dung"] = email["noi_dung"].replace(chuoi_cu, chuoi_moi)
    noi_dung_mail_moi = email["noi_dung"]

    # Kiểm tra xem bản thay đổi với bản gốc có khác nhau không
    if noi_dung_mail_moi != noi_dung_mail_cu:
        # Hiển thị nội dung email sau khi thay thế
        print("Nội dung email sau khi thay đổi:")
        print(email["noi_dung"])
    else:
        print("Nội dung chưa bị thay đổi!")




def luu_ket_qua_thong_ke(tep_moi, danh_sach_email):
    # Mở file với chế độ 'a' (append) để thêm dữ liệu vào cuối file
    with open(tep_moi, 'a') as file:
        # Chuyển danh_sach_email thành chuỗi JSON và ghi vào file
        file.write(json.dumps(danh_sach_email, ensure_ascii=False, indent=4))
        file.write("\n")  # Thêm một dòng mới sau khi ghi xong
















































































