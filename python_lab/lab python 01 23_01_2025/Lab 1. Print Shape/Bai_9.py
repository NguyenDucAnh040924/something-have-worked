# Bài 9: Viết chương trình Python để 
# in ra hình thoi đặc có đường chéo dài d1 
# và đường chéo ngắn
# d2 (do người dùng nhập).

def draw_rhombus(d1, d2):
    """
    Vẽ hình thoi đặc có đường chéo dài d1 và đường chéo ngắn d2.

    Args:
        d1: Độ dài đường chéo dài.
        d2: Độ dài đường chéo ngắn.
    """

    for i in range(d1):
        for j in range(d1):
            if abs(i - d1//2) + abs(j - d1//2) <= d2//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Nhập dữ liệu từ người dùng

# d1 = int(input("Nhập độ dài đường chéo dài: "))
# d2 = int(input("Nhập độ dài đường chéo ngắn: "))

d1 = 5
d2 = 3

# Vẽ hình thoi
draw_rhombus(d1, d2)