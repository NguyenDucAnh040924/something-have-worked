# Write a program to print the multiplication table of a given number

n = input('nhap n: ')

if not n.strip():
    n = 9
else:
    n = int(n)


for i in range(1,11):
    print(f'{n} * {i} = {n*i}')