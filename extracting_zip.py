import zipfile
import os

# Path to your ZIP file
zip_file_path = '/workspaces/Testing_json/New folder.zip'

# Directory where the extracted files will be stored
extract_to_path = 'extracted_files'

# Create the directory if it doesn't exist
if not os.path.exists(extract_to_path):
    os.makedirs(extract_to_path)

# Extract all files from the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"Files extracted to: {extract_to_path}")
