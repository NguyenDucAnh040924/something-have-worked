# Bài 2: Viết chương trình Python để in ra hình chữ nhật rỗng có chiều dài m và chiều rộng n (do
# người dùng nhập).


m = 6
n = 5

for i in range(1,m):
    for j in range(1,n):
        if i == 1 or i == m-1 or j == 1 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")