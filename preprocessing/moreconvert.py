import os
import gzip
import shutil
from pathlib import Path

# Base directory where dataset folders are located
base_dir = Path('C:/Users/BMU/Downloads/osfstorage-archive')

# Function to extract GZ file
def extract_gz_file(gz_file_path, output_file_path):
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Iterate through dataset folders (test, training, validation)
for dataset_type in ['test', 'training', 'validation']:
    dataset_path = base_dir / f'dataset-verse19-{dataset_type}'
    
    # Check if dataset path exists
    if not dataset_path.exists():
        print(f'{dataset_path} not found. Skipping...')
        continue
    
    # Define paths for rawdata and derivatives
    rawdata_path = dataset_path / 'rawdata'
    derivatives_path = dataset_path / 'derivatives'
    
    # Define output directory for extracted data
    output_dir = Path(f'C:/Users/BMU/Downloads/extracted/{dataset_type}')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process rawdata folder
    if rawdata_path.exists():
        for subfolder in rawdata_path.iterdir():
            if subfolder.is_dir() and subfolder.name.startswith('sub-verse'):
                sub_id = subfolder.name.split('-')[-1]
                gz_file_path = next(subfolder.glob('*.gz'), None)
                
                if gz_file_path and gz_file_path.exists():
                    # Construct the output file path
                    output_file_path = output_dir / f'verse{sub_id}.nii'
                    # Extract and save the file
                    extract_gz_file(gz_file_path, output_file_path)
                    print(f'Extracted: {gz_file_path} to {output_file_path}')
                else:
                    print(f'No GZ file found in: {subfolder}')
    else:
        print(f'Rawdata path not found: {rawdata_path}')
    
    # Process derivatives folder (if needed)
    # Add logic here if you have files to extract from derivatives
    
    # Example: Extracting from derivatives
    if derivatives_path.exists():
        for file in derivatives_path.glob('*'):
            # Example extraction logic from derivatives
            # Adjust as per your specific needs
            pass

print('Extraction complete.')
