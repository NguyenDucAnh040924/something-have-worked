from management.xu_ly_chuc_nang import *

menu_list = ["Test f1 (1 mark)","Test f2 (2 mark)", "Test f3 (1 mark)"]
output = "output".upper()
finish = "finish".upper()
exit_msg = "Thoát CT thành công!"
while True:
    index = 0
    for menu in menu_list:
        index += 1
        print("{}. {}".format(index,menu))

    print("============================================")
    lua_chon = input("Your selection (1 -> 3): ")
    match lua_chon:
        
        case '1': 
            # Print the list of employees
            print(output)
            f1(employee_list)
            print(finish)
        case '2':
            print(output)
            # Sort employee by decreasing age
            # Print the list of employees after the sorting
            f2(employee_list)
            print(finish)
        case '3':
            print(output)
            # Find all employees whose age >= 18, 
            # and sort those employees by decreasing salary
            # Print the list of employees after the sorting
            f3(employee_list)
            print(finish)
        case _:
            print(exit_msg)
            break





