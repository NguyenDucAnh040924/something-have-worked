# Bài 4: Viết chương trình Python để in ra hình tam giác vuông cân rỗng có chiều cao h (do người
# dùng nhập).

h = 7

for i in range(1,h):
    for j in range(1,i):
        if i == 1 or i == h-1 or j==1 or j == i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")