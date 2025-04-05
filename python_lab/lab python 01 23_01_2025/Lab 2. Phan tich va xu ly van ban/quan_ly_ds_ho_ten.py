def chuan_hoa_ho_ten(ho_ten):
    # Loai bo khoang trang thua
    ho_ten = ho_ten.strip()

    # Chuyen hoa thanh chu thuong
    ho_ten = ho_ten.lower()

    # Viet hoa chu cai dau
    ho_ten = ho_ten.title()

    return ho_ten


def sap_xep_ho_ten(danh_sach_ho_ten):

    # Sap xep theo ho ten day du
    danh_sach_sap_xep_day_du = sorted(danh_sach_ho_ten)

    # Sap xep theo ten (tu cuoi cung trong ho ten)
    danh_sach_sap_xep_theo_ten = sorted(danh_sach_ho_ten, key=lambda ten: ten.split()[-1])

    return danh_sach_sap_xep_day_du, danh_sach_sap_xep_theo_ten














