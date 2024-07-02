import os
import gzip
import shutil

# Paths
base_dir = '/path/to/data'
output_dir = '/path/to/extracted/labels'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through subfolders
for subfolder in os.listdir(base_dir):
    subfolder_path = os.path.join(base_dir, subfolder)
    if os.path.isdir(subfolder_path) and subfolder.startswith('sub-verse'):
        sub_id = subfolder.split('-')[-1]
        for file in os.listdir(subfolder_path):
            if file.endswith('.gz'):
                gz_file_path = os.path.join(subfolder_path, file)
                # Extract GZ file
                with gzip.open(gz_file_path, 'rb') as f_in:
                    # Assuming the GZ file contains a single NIfTI file
                    nii_filename = f'{sub_id}.nii'
                    nii_file_path = os.path.join(output_dir, nii_filename)
                    with open(nii_file_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                print(f'Extracted: {gz_file_path} to {nii_file_path}')
