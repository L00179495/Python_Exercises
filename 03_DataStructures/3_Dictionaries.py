#Program demonstrates use of Dictionaries

#Creating a dictionary for Students
student = {
    'name': 'John',
    'age': 20,
    'department': 'Computer Science',
    'gpa': 3.8
}

# Accessing dictionary values
print(student['name'])    # John
print(student['age'])     # 20
print(student['department'])   # Computer Science
print(student['gpa'])     # 3.8

# Modifying dictionary values
student['age'] = 21       # Updating age to 21
student['gpa'] = 3.9      # Updating GPA to 3.9

# Adding new key-value pair
student['university'] = 'ATU University'

# Removing a key-value pair
del student['department']

# Accessing dictionary keys and values
print(student.keys())     # ['name', 'age', 'gpa', 'university']
print(student.values())   # ['John', 21, 3.9, 'ATU University']

# Checking if a key exists in the dictionary
print('name' in student)  # True
print('department' in student) # False