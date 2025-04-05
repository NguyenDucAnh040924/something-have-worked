import json

# Giả sử dữ liệu JSON từ API được lưu trong tệp demoAPI_random_user.txt
with open('demoAPI_random_user.txt', 'r') as file:
    # Đọc và chuyển đổi dữ liệu từ JSON
    data = json.load(file)

# Duyệt qua danh sách "results" trong dữ liệu
for person in data["results"]:
    # Lấy thông tin giới tính
    gender = person.get("gender", "Unknown")
    # Lấy thông tin họ tên đầy đủ
    full_name = f'{person["name"]["title"]} {person["name"]["first"]} {person["name"]["last"]}'
    # Lấy địa chỉ
    address = f'{person["location"]["street"]["number"]} {person["location"]["street"]["name"]}, {person["location"]["city"]}, {person["location"]["state"]}, {person["location"]["country"]}'
    # Lấy email
    email = person.get("email", "No email provided")
    # Lấy số điện thoại
    phone = person.get("phone", "No phone provided")
    # Lấy liên kết ảnh đại diện
    picture_url = person["picture"]["large"]

    # In ra thông tin chi tiết
    print("Thông tin người dùng:")
    print(f"  Giới tính: {gender}")
    print(f"  Họ tên: {full_name}")
    print(f"  Địa chỉ: {address}")
    print(f"  Email: {email}")
    print(f"  Số điện thoại: {phone}")
    print(f"  Ảnh đại diện: {picture_url}")
    print("-" * 50)
