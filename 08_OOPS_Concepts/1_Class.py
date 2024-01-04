#Program to creating a class and instantiating a class
class Person:
    # Class variable
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating instances of the Person class
person1 = Person(name="Peter", age=25)
person2 = Person(name="Charles", age=30)

# Accessing attributes and calling methods
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} belongs to the {person2.species} species.")

person1.greet()
person2.greet()
