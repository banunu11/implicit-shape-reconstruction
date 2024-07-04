import os
import shutil
from pathlib import Path

def sort_files(input_dir: str, txt_file: str, output_dir_listed: str, output_dir_not_listed: str):
    # Convert paths to Path objects
    input_dir = Path(input_dir)
    txt_file = Path(txt_file)
    output_dir_listed = Path(output_dir_listed)
    output_dir_not_listed = Path(output_dir_not_listed)
    
    # Ensure output directories exist
    output_dir_listed.mkdir(parents=True, exist_ok=True)
    output_dir_not_listed.mkdir(parents=True, exist_ok=True)
    
    # Read listed filenames from the text file and add .nii extension
    with txt_file.open('r') as f:
        listed_files = {line.strip() + '.nii.gz' for line in f if line.strip()}
    
    # Iterate over all .nii files in the input directory
    for nii_file in input_dir.glob('*.nii.gz'):
        # Check if the file is listed in the text file (with .nii extension)
        if nii_file.name in listed_files:
            target_dir = output_dir_listed
        else:
            target_dir = output_dir_not_listed
        
        # Move the file to the target directory
        shutil.move(str(nii_file), target_dir / nii_file.name)
        print(f'Moved {nii_file.name} to {target_dir}')
    
    print("File sorting completed.")

# Example usage
input_dir = r'C:\Users\ella2\Downloads\thingy\data'
txt_file = r'C:\Users\ella2\Desktop\academic ish\Others\computer science things\summer\implicit-shape-reconstruction\casename_files\verse19\test_cases.txt'
output_dir_listed = r'C:\Users\ella2\Downloads\thingy\data\labels_test'
output_dir_not_listed = r'C:\Users\ella2\Downloads\thingy\data\labels'

sort_files(input_dir, txt_file, output_dir_listed, output_dir_not_listed)
