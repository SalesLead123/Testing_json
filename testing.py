import json

# Path to your JSON file
file_path = ''

# Load the JSON file
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract and print data for each person
for person in data:
    name = person.get('n', 'No name provided')
    address = person.get('a', 'No address provided')
    linkedin_id = person.get('liid', 'No LinkedIn ID provided')
    linkedin_url = person.get('linkedin', 'No LinkedIn URL provided')
    
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"LinkedIn ID: {linkedin_id}")
    print(f"LinkedIn URL: {linkedin_url}")
    
    # Handle optional fields like phone numbers or emails
    if 't' in person:
        phone_numbers = person.get('t')
        print(f"Phone numbers: {phone_numbers}")
    
    if 'e' in person:
        emails = person.get('e')
        print(f"Emails: {emails}")
    
    print('---')  # Divider for clarity
