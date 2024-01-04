#Program demonstrates different String Manipulation

# String Concatenation
name = "Sorna"
age = 25
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)

# String Length
text = "Hello, world!"
length = len(text)
print("Length of the string:", length)

# String Slicing
text = "Hello, world!"
substring = text[7:12]
print("Substring:", substring)

# String Formatting
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print("String formatted->",message)

# String Methods
text = "Hello, world!"
uppercase = text.upper()
lowercase = text.lower()
capitalized = text.capitalize()
reversed_text = text[::-1]
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Capitalized:", capitalized)
print("Reversed:", reversed_text)