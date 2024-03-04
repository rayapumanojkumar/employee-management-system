class Department:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee):
        self.__employees.remove(employee)

    def list_employees(self):
        print(f"Employees in {self.__name} department:")
        for employee in self.__employees:
            print(employee)


