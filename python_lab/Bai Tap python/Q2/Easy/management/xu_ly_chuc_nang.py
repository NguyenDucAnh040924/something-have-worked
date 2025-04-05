import datetime


# 1. Write a program to read a text file and print the number of words in it.
def dem_tu(text_file):

    so_luong_tu = 0

    with open (text_file, 'r') as file: 
        for line in file:
            danh_sach_tu = line.strip().split()
            so_luong_tu += len(danh_sach_tu)
  
    return so_luong_tu


# 2. Write a program to create a new file and write "Hello, World!" to it.
def creat_new_file(file_name):

    try:
        with open(file_name, 'a') as create_file:
            create_file.write("Hello world! ")

        print("Tạo file thành công! ")
    except FileExistsError:
        print("File đã tồn tại! Nhập tên khác để tạo file! ")


# 3. Write a program to read a text file 
# and print all lines that contain a specific word.

def read_file(text_file, key_word):

    danh_sach = []

    try:
        with open(text_file, 'r') as read_file:
            for line in read_file:

                if key_word in line:
                    danh_sach.append(line.strip())
    except FileNotFoundError:
        print(f"Tệp {text_file} không tồn tại. Vui lòng kiểm tra lại! ")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

    return danh_sach
        

# 4. Write a program to copy the content of one text file to another, 
# but in reverse order.

def copy_content(tep_nguon, tep_dich):

    try:
        with open(tep_nguon, 'r') as copy_src:
            lines = copy_src.readlines() # Lưu toàn bộ các dòng vào danh sách

        reversed_lines = lines[::-1]

        try:
            with open(tep_dich, 'w') as ghi_src:
                ghi_src.writelines(reversed_lines)

        except FileNotFoundError:
            with open(tep_dich, 'a') as ghi_src:
                ghi_src.writelines(reversed_lines)
        print(f"Ghi file '{tep_dich}' thành công! ")
    except FileNotFoundError:
        print(f"Tệp '{tep_nguon}' không tồn tại. Vui lòng kiểm tra lại! ")
    except Exception as e:
        print(f"Đã xảy ra lỗi {e}")


# 5. Write a program to create a new text file 
# and write the current date and time to it.
def date_and_time(ten_tep):

    current = datetime.datetime.now()


    formatted_time = current.ctime()

    try:
        try:
            with open (ten_tep, 'w') as ghi_file:
                ghi_file.write(f"Current Date and Time: {formatted_time}\n")
        except FileNotFoundError:
            with open (ten_tep, 'a') as ghi_file:
                ghi_file.write(f"Current Date and Time: {formatted_time}\n")
        print("Ghi thành công! ")
    except FileNotFoundError:
        print(f"File {ten_tep} không tồn tại! Kiểm tra lại! ") 
    except Exception as e:
        print(f"Gặp lỗi {e}")

    return formatted_time

# 6. Write a program to read a text file 
# and print the longest line in the file.

def read_and_take_longest_line(text_file):

    max_length = 0
    longest_line = ""

    try:
        with open(text_file, 'r') as file:
            
            for line in file:
                line_length = len(line.strip()) # Loại bỏ khoảng trắng thừa ở đầu và cuối
                if line_length > max_length:
                    max_length = line_length
                    longest_line = line.strip() # Lưu dòng dài nhất hiện tại
        return max_length, longest_line

    except FileExistsError:
        print(f"File {text_file} không tồn tại! ")

# 7. Write a program to append a new line to an existing text file.
def append_new_line(ten_file, new_line):
    
    try:
        with open(ten_file, 'a') as file:
            file.write(new_line+"\n")
        print(f"Đã thêm dong mới vào file {ten_file}")
    except FileExistsError:
        print(f"File {ten_file} không tồn tại! ")
    except Exception as e:
        print(f"Đã xảy ra lỗi {e}")


# 8. Write a program to rename a file.
def rename_file(current_file_name, new_name_file):
    import os

    os.rename(current_file_name,new_name_file)


# 12. Write a program to check if a file exists
def is_file_existed(ten_file):
    import os

    if os.path.isfile(ten_file):
        print(f"Tên file '{ten_file}' tồn tại! ")
    else:
        print(f"Tên file '{ten_file}' không tồn tại! ")

# 13. Write a program to create a new directory.
def creat_new_folder(ten_folder):

    import os

    if not ten_folder:
        print("Tên folder không được trống! ")
        return

    if os.path.isdir(ten_folder):
        print(f"Thư mục '{ten_folder}' tồn tại! ")
    else:
        os.mkdir(ten_folder)
    

# 15. Write a program to list all files in a directory.
def list_all_file_direct(folder_name):
    import os

    if not folder_name:
        print("Tên thư mục không được bỏ trống!")
        return
    
    if os.path.isdir(folder_name):  # Kiểm tra xem có phải là thư mục không
        files = os.listdir(folder_name)  # Lấy danh sách tất cả các mục trong thư mục
        if len(files) == 0:
            print(f"Thư mục '{folder_name}' rỗng!")
        else:
            print(f"Danh sách các tệp trong thư mục '{folder_name}':")
            for file in files:
                file_path = os.path.join(folder_name, file)
                if os.path.isfile(file_path):  # Kiểm tra nếu là tệp
                    print(file)
    else:
        print(f"'{folder_name}' không phải là một thư mục hợp lệ!")


# 16. Write a program to move a file from one directory to another.
def move_file(src_file, destination_folder):

    import os, shutil

    if not src_file or not destination_folder:
        print(f"Tên file/folder không được để trống! ")
        return
    
    if os.path.isfile(src_file) and os.path.isdir(destination_folder):

        try:
            # Di chuyển tệp từ src_file đến destination_folder
            shutil.move(src_file, destination_folder)
            print(f"Tệp '{src_file}' đã được di chuyển đến '{destination_folder}'")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi di chuyển tệp: {e}")














































































































































































