class Employee:
    def __init__(self, name, emp_id, title, department):
        self.__name = name
        self.__emp_id = emp_id
        self.__title = title
        self.__department = department

    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"ID: {self.__emp_id}")
        print(f"Title: {self.__title}")
        print(f"Department: {self.__department}")

    def __str__(self):
        return f"{self.__name} - ID: {self.__emp_id}"
