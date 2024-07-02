import os
import gzip
import shutil
from pathlib import Path

# Paths
base_dir = Path('downloads/osfstorage-archive')
output_dir = Path('downloads/extracted/labels')

# Create output directory if it doesn't exist
output_dir.mkdir(parents=True, exist_ok=True)

# Function to extract GZ file
def extract_gz_file(gz_file_path, output_file_path):
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Iterate through dataset folders (test, training, validation)
for dataset_type in ['test', 'training', 'validation']:
    dataset_path = base_dir / f'dataset-verse19-{dataset_type}'
    rawdata_path = dataset_path / 'rawdata'
    
    # Iterate through subfolders in rawdata
    for subfolder in rawdata_path.iterdir():
        if subfolder.is_dir() and subfolder.name.startswith('sub-verse'):
            sub_id = subfolder.name.split('-')[-1]
            gz_file_path = subfolder / f'{subfolder.name}.gz'
            
            if gz_file_path.exists():
                # Construct the output file path
                output_file_path = output_dir / f'verse{sub_id}.nii'
                # Extract and save the file
                extract_gz_file(gz_file_path, output_file_path)
                print(f'Extracted: {gz_file_path} to {output_file_path}')

print('Extraction and renaming complete.')
