import os
import glob
from typing import Any
from pathlib import Path




def list_folders(directory: Any) -> list[str] | str:
    try:
        return [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    except FileNotFoundError:
        return "Directory not found."
    except PermissionError:
        return "Permission denied."

def has_directories(directories: Any) -> bool:
    if len (list_folders(directories))>0:
        return True
    else:
        return False

def list_jpg_files_glob(directory: Any) -> str | list[str]:
    try:
        return [os.path.basename(file) for file in glob.glob(os.path.join(directory, "*.jpg"))]
    except FileNotFoundError:
        return "Directory not found."
    except PermissionError:
        return "Permission denied."

def has_files(directory: Any) -> bool:
    if len(list_jpg_files_glob(directory))>0:
        return True
    else:
        return False


def create_folder(folder_name: Any,
                  path: Any) -> bool:
    try:
        parent_directory = Path(path)
        folder_name = folder_name
        folder_path = parent_directory / folder_name

        folder_path.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating folder: {e}")

        return False


def create_python_file(file_path,code):
    # Ensure the directory exists
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Create the .py file
        with open(file_path, "w") as file:
            file.write(code)

        print(f"Python file created at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating Python file: {e}")
        return False


def create_folder(folder_name,path):
    try:
        parent_directory = Path(path)
        folder_name = folder_name
        folder_path = parent_directory / folder_name

        folder_path.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating folder: {e}")
        return False