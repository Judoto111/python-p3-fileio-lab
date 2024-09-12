# lib/file_io.py

from pathlib import Path

def write_file(file_name, file_content):
    """
    Write content to a .txt file. Overwrites existing file with the same name.
    
    Args:
    file_name (str or Path): The name of the file (without extension).
    file_content (str): The content to write to the file.
    """
    if isinstance(file_name, Path):
        file_name = str(file_name)
    with open(file_name + '.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Append content to a .txt file. Creates the file if it does not exist.
    
    Args:
    file_name (str or Path): The name of the file (without extension).
    append_content (str): The content to append to the file.
    """
    if isinstance(file_name, Path):
        file_name = str(file_name)
    with open(file_name + '.txt', 'a') as file:
        file.write(append_content)  # Ensure no extra newline is added

def read_file(file_name):
    """
    Read content from a .txt file.
    
    Args:
    file_name (str or Path): The name of the file (without extension).
    
    Returns:
    str: The content of the file.
    """
    if isinstance(file_name, Path):
        file_name = str(file_name)
    with open(file_name + '.txt', 'r') as file:
        return file.read()
