# Bài 5: Viết chương trình Python để in ra hình tam giác cân đặc có chiều cao h (do người dùng
# nhập).

h = 7

for i in range(1,h):
    for j in range(1,2*h-1):
        if j >=h-i+1 and j<=h+i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")