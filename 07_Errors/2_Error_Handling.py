#Program for Error Handling
import os
def create_directory(directory_name: str)->int: 
    # Check to see if the directory already exists
    if os.path.isdir(directory_name):
        # The directory already exists
        return 2
    else:
        # Use try/except to catch errors
        try:
            # Create the directory
            os.mkdir(directory_name)
            # If this worked, return True
            return 0
        except:
            # Give an explicit error message
            print(f"Error creating directory {directory_name}")
            # If this did not work, return False
            return 1

if (__name__ == '__main__'):

    if create_directory("Testing") == 0:
        print("Creating a directory worked")
            # Do other stuff
    elif create_directory("Testing") == 1:
            print("You couldn't create a directory!")
            # Do other stuff
    elif create_directory("Testing") == 2:
            print("Directory already existed!")
            # Do other stuff
    else:
         print('')

