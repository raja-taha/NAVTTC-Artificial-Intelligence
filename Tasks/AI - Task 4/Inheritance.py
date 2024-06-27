class Person:
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call the constructor of the base class
        super().__init__(name, age)
        # Additional instance variables
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        # Display person details using the method from the base class
        super().display_person_details()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


# Create an instance of the Employee class
employee2 = Employee("Jane Smith", 30, "E123", 60000)

# Display employee details
employee2.display_employee_details()
