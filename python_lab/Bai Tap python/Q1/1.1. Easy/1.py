# Write a program to print all odd numbers from 1 to 50.

ls = []
# Nhập n (hoặc để trống để mặc định là 50)
n = input('Nhap n: ')

# Gán giá trị mặc định nếu không nhập
if not n.strip():
    n = 50
else:
    n = int(n)

for i in range(1,n+1):
    if i % 2 == 1:
        ls.append(str(i))

print(' '.join(ls))