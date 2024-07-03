import os
import re

# Path to the directory containing the files to be renamed
folder_path = r'C:\Users\ella2\Downloads\thingy\extracted\derivatives\validation'  # Replace with your folder path

# Regular expression to match files starting with "verseverse" followed by three digits
pattern = re.compile(r'^verseverse(\d{3})')

# Iterate through all files in the specified directory
for filename in os.listdir(folder_path):
    # Match the pattern
    match = pattern.match(filename)
    if match:
        # Extract the three-digit number
        number = match.group(1)
        # Construct the new filename
        new_filename = f'verse{number}.nii'
        # Get full file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} to {new_filename}')
    else:
        print(f'No match for: {filename}')

print('Renaming complete.')
