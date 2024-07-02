import os
import gzip
import shutil
from pathlib import Path

# Paths
base_dir = Path('C:/Users/BMU/Downloads/osfstorage-archive')
output_dir = Path('C:/Users/BMU/Downloads/extracted/labels')

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
    
    if not rawdata_path.exists():
        print(f'Raw data path does not exist: {rawdata_path}')
        continue
    
    # Iterate through subfolders in rawdata
    for subfolder in rawdata_path.iterdir():
        if subfolder.is_dir() and subfolder.name.startswith('sub-verse'):
            sub_id = subfolder.name.split('-')[-1]
            gz_file_path = next(subfolder.glob('*.gz'), None)
            
            if gz_file_path and gz_file_path.exists():
                # Construct the output file path
                output_file_path = output_dir / f'verse{sub_id}.nii'
                # Extract and save the file
                try:
                    extract_gz_file(gz_file_path, output_file_path)
                    print(f'Extracted: {gz_file_path} to {output_file_path}')
                except Exception as e:
                    print(f'Failed to extract {gz_file_path}: {e}')
            else:
                print(f'No GZ file found in: {subfolder}')

print('Extraction and renaming complete.')
