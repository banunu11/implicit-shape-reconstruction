import os
import shutil
from pathlib import Path

def move_segmentation_files(source_dir, target_dir):
    """
    Moves all files with '_seg' in their names from the source directory to the target directory.

    :param source_dir: Path to the source directory.
    :param target_dir: Path to the target directory.
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Ensure the target directory exists
    target_path.mkdir(parents=True, exist_ok=True)

    # Iterate through files in the source directory
    for file in source_path.iterdir():
        if file.is_file() and '_seg' in file.name:
            shutil.move(str(file), target_path / file.name)
            print(f'Moved: {file.name} to {target_path}')

if __name__ == "__main__":
    source_directory = r'C:\Users\ella2\Downloads\thingy\osfstorage-archive\03_test'  # Replace with your source directory
    target_directory = r'C:\Users\ella2\Downloads\thingy\osfstorage-archive\testing_seg'  # Replace with your target directory

    move_segmentation_files(source_directory, target_directory)
