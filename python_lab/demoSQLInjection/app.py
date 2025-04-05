import sqlite3
import tkinter as tk
from tkinter import messagebox
import log
import socket
import threading
import checkLog  # Import checkLog.py

# Lấy địa chỉ IP của máy client
def get_ip():
    return socket.gethostbyname(socket.gethostname())

# Hàm kiểm tra thông tin đăng nhập
def login(event=None):
    username = entry_user.get()
    password = entry_pass.get()
    user_ip = get_ip()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        log.write_log(username, user_ip, "Success")
        messagebox.showinfo("Login", "Đăng nhập thành công!")
    else:
        log.write_log(username, user_ip, "Failed")
        messagebox.showerror("Login", "Sai tài khoản hoặc mật khẩu!")

    # ✅ Chạy checkLog.py mỗi khi có input mới
    threading.Thread(target=checkLog.detect_sql_injection, daemon=True).start()

# Tạo giao diện
root = tk.Tk()
root.title("Login App")
root.geometry("400x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="w", pady=5)
entry_user = tk.Entry(frame)
entry_user.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="w", pady=5)
entry_pass = tk.Entry(frame, show="*")
entry_pass.grid(row=1, column=1, pady=5)

btn_login = tk.Button(frame, text="Login", command=login)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)

# Hỗ trợ phím Enter để đăng nhập
root.bind("<Return>", login)

root.mainloop()
