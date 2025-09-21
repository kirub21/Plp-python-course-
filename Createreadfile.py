def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except Exception as e:
        print(f"Could not write to file '{new_filename}': {e}")

if __name__ == "__main__":
    read_and_modify_file()
