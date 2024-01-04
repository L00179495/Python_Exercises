#Program for inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Calling the constructor of the base class (Person)
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        # Overriding the display_info method of the base class
        base_info = super().display_info()
        return f"{base_info}, Employee ID: {self.employee_id}"

# Creating instances of the subclasses
person = Person(name="Nitish", age=30)
employee = Employee(name="Nishita", age=35, employee_id="EMP123")

# Accessing attributes and calling methods
print(person.display_info())
print(employee.display_info())
