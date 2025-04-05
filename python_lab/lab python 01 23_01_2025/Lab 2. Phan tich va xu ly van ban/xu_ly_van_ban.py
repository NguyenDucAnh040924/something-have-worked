def chuan_hoa_van_ban(van_ban):
    #Chuyen thanh chu thuong
    van_ban = van_ban.lower()
    # return van_ban

    # Loai bo ky tu dac biet
    ky_tu_dac_biet = [",",".","!","?","*"]
    for ky_tu in ky_tu_dac_biet:
        van_ban = van_ban.replace(ky_tu," ")

    return van_ban


def phan_tich_van_ban(van_ban):
    # Tach tu
    danh_sach_tu = van_ban.split()

    # Dem so tu
    so_luong_tu = len(danh_sach_tu)

    # Tim tu ngan va dai nhat
    tu_dai_nhat = ""
    tu_ngan_nhat = danh_sach_tu[0] #Khoi tao ban dau

    for tu in danh_sach_tu:
        if len(tu) > len(tu_dai_nhat):
            tu_dai_nhat = tu
        if len(tu) < len(tu_ngan_nhat):
            tu_ngan_nhat = tu 


    # Dem so lan xuat hien cua tung tu
    tan_suat_tu = {}
    for tu in danh_sach_tu:
        if tu in tan_suat_tu:
            tan_suat_tu[tu] = tan_suat_tu[tu] + 1
        else:
            tan_suat_tu[tu] = 1

    return so_luong_tu, tu_dai_nhat, tu_ngan_nhat, tan_suat_tu



def xu_ly_van_ban(van_ban, tu_can_thay_the, tu_thay_the):


    # Thay the tu
    van_ban_moi = van_ban.replace(tu_can_thay_the, tu_thay_the)

    # Dao nguoc thu tu tu
    danh_sach_tu = van_ban_moi.split()
    danh_sach_tu.reverse()
    van_ban_dao_nguoc = " ".join(danh_sach_tu)

    # Kiem tra Palindrome
    van_ban_chuan_hoa = chuan_hoa_van_ban(van_ban) # Chuan hoa truoc khi kiem tra
    la_palindrome = van_ban_chuan_hoa == van_ban_chuan_hoa[::-1] # Kiem tra chuoi dao nguoc

    return van_ban_dao_nguoc, la_palindrome



