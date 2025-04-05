# Bài 8: Viết chương trình Python để in ra hình 
# kim tự tháp rỗng có chiều cao h (do người dùng nhập).



h = 7

for i in range(1,h+1):
    for j in range(1,2*h):
        if i == h or j == h-i+1 or j == h+i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")