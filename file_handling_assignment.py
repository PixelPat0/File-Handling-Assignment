# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Line 1: Top of the morning to ya! \n")
            file.write("Line 2: 182201996375 \n")
            file.write("Line 3: In case I don't see ya, good afternoon, good-evening, and goodnight! \n")
        print("File 'my_file.txt' created successfully.")
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    finally:
        print("File creation process completed.")


# This is the function to read the contents of the file and display them
def read_file(filename="my_file.txt"):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            for line in file:
                print(line.strip()) #removing whitespaces for cleaner look
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")

#this is the function to append the file
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: This line is a result of the append method \n")
            file.write("Line 5: 2598748945165 \n")
            file.write("Line 6: What about second breakfast? \n")
        print("Content has been appended to 'my_file.txt' successfully!")
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")


create_file()
read_file()
append_file()
