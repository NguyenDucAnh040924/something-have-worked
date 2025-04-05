class Employee:
    def __init__(self, name, salary, age):
        self._name = None  # Thuộc tính private cho name
        self._salary = None  # Thuộc tính private cho salary
        self._age = None  # Thuộc tính private cho age

        # Sử dụng setter để kiểm tra giá trị ban đầu
        self.name = name
        self.salary = salary
        self.age = age

    # Getter cho name
    @property
    def name(self):
        return self._name

    # Setter cho name
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
        else:
            raise ValueError("Họ tên không thể trống")

    # Getter cho age
    @property
    def age(self):
        return self._age

    # Setter cho age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age phải lớn hơn 0!")
        else:
            self._age = value

    # Getter cho salary
    @property
    def salary(self):
        return self._salary

    # Setter cho salary
    @salary.setter
    def salary(self, value):
        if value <= 100:
            raise ValueError("Lương phải lớn hơn 100!")
        else:
            self._salary = value

    def hien_thi_thong_tin(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Age: {self.age}")
