import json
import re

# Path to your text file (containing dictionaries in each line)
file_path = 'Untitled.txt'

# List to store all dictionaries
data_list = []

def fix_malformed_line(line):
    """
    Function to clean up the line by converting malformed fields into valid JSON structure.
    """
    # Fix phone numbers: replace incorrect phone entries with a list
    line = re.sub(r'"t":"([^"]+)",([^"]+)",([^"]+)",([^"]+)",([^"]+)",([^"]+)",([^"]+)"', 
                  r'"t":["\1", "\2", "\3", "\4", "\5", "\6", "\7"]', line)
    
    # Fix emails: ensure emails are stored in a list
    line = re.sub(r'"e":"([^"]+)","([^"]+)"', r'"e":["\1", "\2"]', line)

    return line

# Open the file and read line by line
with open(file_path, 'r') as file:
    for line in file:
        try:
            # Fix the line before attempting to parse it
            fixed_line = fix_malformed_line(line.strip())
            # Parse each line as a JSON object (dictionary)
            data = json.loads(fixed_line)
            data_list.append(data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e} for line: {line}")

# Process the data (for example, print or extract specific keys)
for person in data_list:
    name = person.get('n', 'No name provided')
    address = person.get('a', 'No address provided')
    linkedin_id = person.get('liid', 'No LinkedIn ID provided')
    linkedin_url = person.get('linkedin', 'No LinkedIn URL provided')

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"LinkedIn ID: {linkedin_id}")
    print(f"LinkedIn URL: {linkedin_url}")

    # Extract phone numbers if available
    if 't' in person:
        phone_numbers = person.get('t')
        print(f"Phone numbers: {phone_numbers}")
    
    # Extract and split emails if available
    if 'e' in person:
        emails = person.get('e')
        print(f"Emails: {emails}")
    
    print('---')  # Divider for clarity
