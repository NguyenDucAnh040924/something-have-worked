from xu_ly_van_ban import *
from quan_ly_ds_ho_ten import *

# -------- CT chinh ----------------

van_ban = input("Nhap doan van ban: ")
tu_can_thay_the = input("Nhap tu can thay the: ")
tu_thay_the = input("Nhap tu thay the: ")

van_ban_chuan_hoa = chuan_hoa_van_ban(van_ban)
so_luong_tu, tu_dai_nhat, tu_ngan_nhat, tan_suat_tu = phan_tich_van_ban(van_ban_chuan_hoa)
van_ban_dao_nguoc, la_palindrome = xu_ly_van_ban(van_ban_chuan_hoa, tu_can_thay_the, tu_thay_the)

print("So luong tu: ",so_luong_tu)
print("Tu dai nhat: ",tu_dai_nhat)
print("Tu ngan nhat: ",tu_ngan_nhat)
print("So lan xuat hien cua tung tu: ",tan_suat_tu)
print("Van ban sau khi thay the va dao nguoc la: ",van_ban_dao_nguoc)


if la_palindrome:
    print("Van ban la palindrome!")
else:
    print("Van ban khong la palindrome!")

danh_sach_ho_ten = []
print("Nhap danh sach ho ten(Nhap done de ket thuc nhap): ")
ho_ten = input()
while ho_ten != "done":
    danh_sach_ho_ten.append(ho_ten)
    ho_ten = input()


# Chuan hoa ho ten
danh_sach_chuan_hoa = []
for ho_ten in danh_sach_ho_ten:
    ho_ten_chuan_hoa = chuan_hoa_ho_ten(ho_ten)
    danh_sach_chuan_hoa.append(ho_ten_chuan_hoa)


# Sap xep ho ten
danh_sach_sap_xep_day_du, danh_sach_sap_xep_theo_ten = sap_xep_ho_ten(danh_sach_chuan_hoa)

print("Danh sach ho ten da chuan hoa va sap xep theo ho ten day du.")
for ho_ten in danh_sach_sap_xep_day_du:
    print(ho_ten)

print("Danh sach ho ten da chuan hoa va sap xep theo ten.")
for ho_ten in danh_sach_sap_xep_theo_ten:
    print(ho_ten)





