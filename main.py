from entities.Company import Company
from entities.Department import Department
from entities.Employee import Employee


def display():
    print("Employee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department Employees")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Departments")
    print("7. Exit")


def main():
    company = Company()
    while True:
        display()
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter employee department: ")
            employee = Employee(name, emp_id, title, department)
            if department in company.get_department():
                company.get_department()[department].add_employee(employee)
            else:
                print("Department does not exist. Please add the department first.")
        elif choice == "2":
            department = input("Enter employee department: ")
            if department in company.get_department():
                department_obj = company.get_department()[department]
                emp_id = input("Enter employee ID to remove: ")
                for employee in department_obj.employees:
                    if employee.emp_id == emp_id:
                        department_obj.remove_employee(employee)
                        print("Employee removed successfully.")
                        break
                else:
                    print("Employee not found.")
            else:
                print("Department does not exist.")
        elif choice == "3":
            department = input("Enter department name to display employees: ")
            if department in company.get_department():
                company.get_department()[department].list_employees()
            else:
                print("Department does not exist.")
        elif choice == "4":
            department_name = input("Enter department name to add: ")
            department = Department(department_name)
            company.add_department(department)
            print("Department added successfully.")
        elif choice == "5":
            department_name = input("Enter department name to remove: ")
            if department_name in company.get_department():
                company.remove_department(department_name)
                print("Department removed successfully.")
            else:
                print("Department does not exist.")
        elif choice == "6":
            company.display_departments()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
