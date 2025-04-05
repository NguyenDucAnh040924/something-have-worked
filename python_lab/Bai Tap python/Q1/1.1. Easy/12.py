# Take a string as input and check if it contains a specific word.

# Nhập chuỗi và từ cần kiểm tra
input_string = input("Nhập một chuỗi: ")
word_to_check = input("Nhập từ cần kiểm tra: ")

# Kiểm tra sự xuất hiện của từ trong chuỗi
if word_to_check in input_string:
    print(f"Từ '{word_to_check}' có trong chuỗi.")
else:
    print(f"Từ '{word_to_check}' không có trong chuỗi.")
