try:
    # Write initial lines to the file
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("The number of items is 42.\n")
        file.write("The price of the item is $19.99.\n")
    print("File 'my_file.txt' created and initial text written successfully.\n")
    
    # Open the file in append mode and add more lines
    with open("my_file.txt", 'a') as file:
        file.write("This is an appended line 1.\n")
        file.write("Here is another appended line 2.\n")
        file.write("Finally, appended line 3 completes the task.\n")
    print("Additional lines appended to 'my_file.txt' successfully.\n")

    # Read from the file and display its contents
    with open("my_file.txt", 'r') as file:
        print("Reading updated contents of 'my_file.txt':")
        contents = file.read()  # Read the entire file content
        print(contents)

# Handle specific file-related exceptions
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to access or modify 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# This block is always executed, whether or not an error occurred
finally:
    print("\nFile handling operation completed.")