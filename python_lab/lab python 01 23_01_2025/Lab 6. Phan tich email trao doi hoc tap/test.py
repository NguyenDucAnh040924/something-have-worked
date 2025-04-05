from phan_tich_email import *

result = doc_email("hoc_tap_email.txt")

# print(f"{result=}")

# def count(result):
#     count: int = 0

#     for senter in result:
#         if isinstance(senter, dict):
#             count += 1
#         print(f"{senter}\n\n")


#     print(f"{count= }")

# thongKe = thong_ke_nguoi_gui(result)

# for t in thongKe:    
#     print(f"{t} {thongKe[t]}")

# r = tim_kiem_email(result, "schedule")

# print(f"{r= }")

# thay_the_noi_dung(3,result, "schedule","LOL")

# thutu = 0
# for thuTu in result:
#     thutu += 1
#     print(f"{thutu}. tieu de= {thuTu['nguoi_gui']}, thu tu= {thuTu['tieu_de']}")

# ket_qua = tim_kiem_email(result, "schedule")


# Lấy danh sách tiêu đề email từ danh sách dictionary
# for line in ket_qua:
#     print(line)


so_luong = dem_tu(3,result)

print(f"{so_luong=}")







