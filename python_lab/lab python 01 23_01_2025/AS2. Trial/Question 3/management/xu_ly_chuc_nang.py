from entity.employee import Employee


employee_list = [["Nguyen Van A",1000,15], ["Tran Van V",1500,18],
                ["Le Van L",2000,50], ["Dang Van M",2500,20],
                ]

def f1(employee_list):

    if not employee_list:
        print("Danh sách employee trống! ")
        return

    index = 0
    for employee in employee_list:
        employee = Employee(employee[0],employee[1],employee[2])
        index += 1
        print(f"Employees {index}")
        employee.hien_thi_thong_tin()


def f2(employee_list):
    
    if not employee_list:
        print("Danh sách employee trống! ")
        return

    size = len(employee_list)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if employee_list[j][2] < employee_list[j+1][2]:

                employee_list[j], employee_list[j+1] = employee_list[j+1], employee_list[j]

    index = 0
    for emp in employee_list:
        index += 1
        print(f"Employees {index}")
        emp = Employee(emp[0],emp[1],emp[2])
        emp.hien_thi_thong_tin()

def f3(employee_list):
    
    if not employee_list:
        print("Danh sách employee trống! ")
        return

    size = len(employee_list)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if employee_list[j][1] < employee_list[j+1][1]:

                employee_list[j], employee_list[j+1] = employee_list[j+1], employee_list[j]

    index = 0
    for emp in employee_list:
        index += 1
        print(f"Employees {index}")
        if emp[2] >= 18:
            emp = Employee(emp[0],emp[1],emp[2])
            emp.hien_thi_thong_tin()

        
