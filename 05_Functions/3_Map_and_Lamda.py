def double_number(n: int)->int:
    """
    Simple function to double a number
    """
    return n+n

# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map 
print(list(result))
# Or iterate through it
for item in map(double_number, my_numbers):
    print(item)

#Lambda: one-line function without the need for a formal function definition
    
circumference = lambda radius : 2 * 3.142 * radius
area = lambda radius : 3.142 * radius * radius
radius = 5
print('circumference value of Circle:',circumference(radius),'Area Value of circle:', area(radius))