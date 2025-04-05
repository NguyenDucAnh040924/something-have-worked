# Create a list of names and sort them alphabetically.

# Tạo danh sách các tên
names = ["Alice", "Bob", "Charlie", "Eve", "David"]

# Sắp xếp theo thứ tự bảng chữ cái mà không dùng hàm sort()
for i in range(len(names)):
    for j in range(0, len(names) - i - 1):
        if names[j] > names[j + 1]:
            # Hoán đổi nếu phần tử hiện tại lớn hơn phần tử tiếp theo
            names[j], names[j + 1] = names[j + 1], names[j]

# Hiển thị kết quả
print("Danh sách sau khi sắp xếp:", names)
