import os
import gzip
import shutil
from pathlib import Path

# converting the new extract vertebra files

def extract_gz_file(gz_file_path, output_dir):
    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract the file name without the .gz extension
    output_file_path = output_dir / gz_file_path.stem

    # Decompress the .gz file
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print(f'Extracted: {gz_file_path} to {output_file_path}')

# Path to the directory containing the .gz files
input_dir = Path(r'C:\Users\ella2\Downloads\thingy\converted\training zip')  # Replace with your folder path

# Path to the output directory (can be the same as input_dir or a different directory)
output_dir = Path(r'C:\Users\ella2\Downloads\thingy\converted\training')  # Replace with your output folder path

# Iterate through all .gz files in the specified directory
for gz_file_path in input_dir.glob('*.gz'):
    extract_gz_file(gz_file_path, output_dir)

print('All files have been extracted.')
