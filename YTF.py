import re

input_file = r"path/to/your/input/file"
output_file = r"/path/to/your/export/file/"

try:
    # Reading from the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    print(f"Successfully read from {input_file}")


    with open(output_file, 'w') as output:
        for i in range(len(lines)):
            if re.match(r'^\d{1,2}:\d{2}', lines[i].strip()):
                if i + 1 < len(lines) and not re.match(r'^\d{1,2}:\d{2}', lines[i + 1].strip()):
                    output.write(lines[i].strip() + "  " + lines[i + 1].strip() + "\n")
                else:
                    output.write(lines[i].strip() + "  ")

        print(f"Successfully wrote to {output_file}")

    print("Transcript formatted successfully!")

except FileNotFoundError as e:
    print(f"Error: The file was not found. Check if the path is correct: {e}")
except PermissionError:
    print("Error: Permission denied. You might not have rights to read/write the file.")
except IOError as e:
    print(f"IO Error: There was an issue with file operations. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
