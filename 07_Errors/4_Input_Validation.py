#Program to validate user input for Integer

def get_valid_integer(prompt):
    """Prompt the user for an integer input and validate it."""
    while True:
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    # Get a valid integer from the user
    age = get_valid_integer("Enter your age: ")

    # Display the entered age
    print(f"Your age is: {age}")

if __name__ == "__main__":
    main()
