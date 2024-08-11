import re

input_file = "/Path/to/your/input/unformatted/transcription/file"
output_file = "/Path/To/Your/Output/File/Name"

with open(input_file, 'r') as file:
    lines = file.readlines()
with open(output_file, 'w') as output:
    for i in range(len(lines)):
        if re.match(r'^\d{1,2}:\d{2}', lines[i].strip()):
            if i + 1 < len(lines) and not re.match(r'^\d{1,2}:\d{2}', lines[i + 1].strip()):
                # Remove newline after the timestamp and add two spaces
                output.write(lines[i].strip() + "  " + lines[i + 1].strip() + "\n")
            else:
                output.write(lines[i].strip() + "  ")
        else:
            continue

print("Transcript formatted successfully!")
