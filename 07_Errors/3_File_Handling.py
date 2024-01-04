#Program to write contents to a new file
def write_to_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to '{filename}' successfully.")

def read_from_file(filename):
    """Read content from a file and print it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content from '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    # Get user input
    user_input = input("Enter content to write to the file: ")

    # Specify the filename
    filename = 'Test_File.txt'

    # Write user input to the file
    write_to_file(filename, user_input)

    # Read content from the file and print it
    read_from_file(filename)

if __name__ == "__main__":
    main()
