# Global variable
global_variable = 5

def my_function():
    # Local variable within the function
    local_variable = 10
    print("Inside function - local_variable:", local_variable)

    # Accessing the global variable within the function
    print("Inside function - global_variable:", global_variable)

# Calling the function
my_function()

# Accessing the global variable outside the function
print("Outside function - global_variable:", global_variable)
