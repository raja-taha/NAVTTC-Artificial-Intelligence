class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: Department has a list of Employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.name}")
        for employee in self.employees:
            print(f"Employee: {employee.name}")

# Create instances of Employee
employee1 = Employee("John")
employee2 = Employee("Jane")

# Create an instance of Department
department = Department("HR")

# Add employees to the department
department.add_employee(employee1)
department.add_employee(employee2)

# Demonstrate aggregation
department.show_employees()
