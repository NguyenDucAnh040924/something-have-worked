import math

def calculate_distance():
    print("Hướng dẫn: Nhập hướng di chuyển (UP, DOWN, LEFT, RIGHT) và số bước cách nhau bởi dấu cách. Nhập 'FINISH' để kết thúc.")

    # Initialize the starting position (0, 0)
    x, y = 0, 0

    while True: 
        movements = input("Nhập hướng và bước (hoặc 'FINISH' để kết thúc): ")

        # Check for finish command
        if movements.strip().upper() == "FINISH":
            print("Thoát chương trình thành công!")
            break

        if not movements:
            movements = [
                ("UP", 1),
                ("DOWN", 5),
                ("LEFT", 9),
                ("RIGHT", 12)
            ]


        try:
            # Split the input and parse direction and steps
            direction, steps = movements.split()
            steps = int(steps)

            # Process each movement
            if direction.upper() == "UP":
                y += steps
            elif direction.upper() == "DOWN":
                y -= steps
            elif direction.upper() == "LEFT":
                x -= steps
            elif direction.upper() == "RIGHT":
                x += steps
            else:
                print("Hướng không hợp lệ! Vui lòng nhập lại.")
                continue

        except ValueError:
            print("Dữ liệu nhập không hợp lệ! Vui lòng nhập đúng định dạng (ví dụ: UP 5).")
            continue

        # Calculate the distance from the origin
        distance = math.sqrt(x**2 + y**2)

        print(f"Vị trí hiện tại: ({x}, {y}), Khoảng cách từ gốc tọa độ: {round(distance)}")

# Run the function
calculate_distance()


def calculate_distance_2():
    print("Hướng dẫn: Nhập hướng di chuyển (UP, DOWN, LEFT, RIGHT) và số bước cách nhau bởi dấu cách. Nhập 'FINISH' để kết thúc.")
    print("Nếu không nhập gì, chương trình sẽ sử dụng dữ liệu mặc định: [('UP', 1), ('DOWN', 5), ('LEFT', 9), ('RIGHT', 12)].")

    # Initialize the starting position (0, 0)
    x, y = 0, 0

    # Default data if no input is provided
    default_movements = [("UP", 1), ("DOWN", 5), ("LEFT", 9), ("RIGHT", 12)]
    use_default = False  # Flag to handle default data

    while True: 
        if not use_default:
            movements = input("Nhập hướng và bước (hoặc 'FINISH' để kết thúc): ").strip()

            # Check for finish command
            if movements.upper() == "FINISH":
                print("Thoát chương trình thành công!")
                break

            # If input is empty, switch to default movements
            if not movements:
                print("Không có dữ liệu nhập. Sử dụng dữ liệu mặc định.")
                use_default = True
                continue
        else:
            # Process default data
            if default_movements:
                direction, steps = default_movements.pop(0)
            else:
                print("Đã hoàn thành xử lý dữ liệu mặc định.")
                break

        try:
            # If not using default, parse user input
            if not use_default:
                direction, steps = movements.split()
                steps = int(steps)

            # Process each movement
            if direction.upper() == "UP":
                y += steps
            elif direction.upper() == "DOWN":
                y -= steps
            elif direction.upper() == "LEFT":
                x -= steps
            elif direction.upper() == "RIGHT":
                x += steps
            else:
                print("Hướng không hợp lệ! Vui lòng nhập lại.")
                continue

        except ValueError:
            print("Dữ liệu nhập không hợp lệ! Vui lòng nhập đúng định dạng (ví dụ: UP 5).")
            continue

        # Calculate the distance from the origin
        distance = math.sqrt(x**2 + y**2)

        print(f"Vị trí hiện tại: ({x}, {y}), Khoảng cách từ gốc tọa độ: {round(distance, 2)}")



# Run the function
calculate_distance_2()










