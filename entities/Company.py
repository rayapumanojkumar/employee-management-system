class Company:
    def __init__(self):
        self.__departments = {}

    def add_department(self, department):
        self.__departments[department.name] = department

    def remove_department(self, department_name):
        del self.__departments[department_name]

    def get_department(self):
        return self.__departments

    def display_departments(self):
        print("Departments:")
        for department_name in self.__departments:
            print(department_name)
