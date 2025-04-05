# Bài 10: Viết chương trình Python để in ra hình chữ X đặc có chiều cao h (do người dùng nhập, h là
# số lẻ).


def draw_x(h):
    """
    Vẽ hình chữ X đặc có chiều cao h.

    Args:
        h: Chiều cao của hình chữ X (phải là số lẻ).
    """

    if h % 2 == 0:
        print("Chiều cao phải là số lẻ!")
        return

    for i in range(h):
        for j in range(h):
            if i == j or i + j == h - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Nhập chiều cao
# h = int(input("Nhập chiều cao của hình chữ X (số lẻ): "))

h = 11

# Vẽ hình chữ X
draw_x(h)