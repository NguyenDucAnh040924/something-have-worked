import re
import time
import datetime
from collections import defaultdict

# Danh sách các từ khóa SQL Injection phổ biến
SQLI_PATTERNS = [
    r"UNION.*SELECT", r"DROP TABLE", r"INSERT INTO", 
    r"UPDATE .* SET", r"' OR '1'='1", r"--", r";"
]

# Lưu số lần thử của từng IP
ip_attempts = defaultdict(list)  # Lưu timestamp của từng lần nhập

def detect_sql_injection():
    global ip_attempts

    try:
        with open("log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        suspicious_ips = set()
        current_time = datetime.datetime.now()  # Lấy thời gian hiện tại

        for line in lines:
            parts = line.strip().split(" - ")
            if len(parts) < 4:
                continue  # Bỏ qua dòng log không đúng định dạng

            timestamp_str, ip, user, status = parts
            
            # Chuyển timestamp từ chuỗi sang datetime
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            for pattern in SQLI_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    # Nếu cú pháp SQL Injection xuất hiện, lưu timestamp
                    ip_attempts[ip].append(timestamp)

                    # Xóa các lần thử cũ (hơn 1 phút trước)
                    ip_attempts[ip] = [t for t in ip_attempts[ip] if (current_time - t).total_seconds() <= 60]

                    # Nếu cùng 1 IP có 3 lần nhập SQL Injection trong 1 phút → Ghi vào hacker.txt
                    if len(ip_attempts[ip]) >= 3:
                        suspicious_ips.add(ip)

                    break  # Chỉ cần khớp 1 pattern là đủ

        # Ghi vào hacker.txt nếu có IP tấn công
        if suspicious_ips:
            with open("noticeHacking.txt", "a", encoding="utf-8") as f:
                for ip in suspicious_ips:
                    f.write(f"[*] {ip} đang cố gắng tấn công SQL Injection!\n")
                    print(f"[*] Cảnh báo: {ip} đang cố attack!")

    except FileNotFoundError:
        print("Không tìm thấy file log.txt!")
    except ValueError as e:
        print(f"Lỗi định dạng timestamp: {e}")

