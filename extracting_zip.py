# a = {"a": "egypt","liid": "saleh-adoum-hamid-1646245a","linkedin": "https://www.linkedin.com/in/saleh-adoum-hamid-1646245a","n": "saleh hamid"}
# for b in a.values():
#     print(b)


import json

# Path to your text file
file_path = 'Untitled.txt'

# List to store all dictionaries
data_list = []

# Open the file and read line by line
with open(file_path, 'r') as file:
    for line in file:
        try:
            # Parse each line as a JSON object (dictionary)
            data = json.loads(line.strip())  # .strip() removes any extra whitespace or newline characters
            data_list.append(data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e} for line: {line}")

# Process the data (for example, print or extract specific keys)
for person in data_list:
    name = person.get('n', 'No name provided')
    address = person.get('a', 'No address provided')
    linkedin_id = person.get('liid', 'No LinkedIn ID provided')
    linkedin_url = person.get('linkedin', 'No LinkedIn URL provided')
    linkedin_email = person.get('e', 'No LinkedIn email provided')

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"LinkedIn ID: {linkedin_id}")
    print(f"LinkedIn URL: {linkedin_url}")
    print(f"LinkedIn email: {linkedin_email}")

    if 't' in person:
        phone_numbers = person.get('t')
        print(f"Phone numbers: {phone_numbers}")
    
    if 'e' in person:
        emails = person.get('e')
        print(f"Emails: {emails}")
    
    print('---')  # Divider for clarity
