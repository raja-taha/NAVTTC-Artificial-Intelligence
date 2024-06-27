class Employee:
    # Class variable
    company_name = "Tech Corp"

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company_name}")


# Create an instance of the Employee class
employee1 = Employee("John Doe", 50000)

# Display employee details
employee1.display_employee_details()

# Accessing class variable directly from the class
print(f"Company Name: {Employee.company_name}")

# Accessing instance variables
print(f"Employee Name: {employee1.name}")
print(f"Employee Salary: {employee1.salary}")
