# test_file_io.py

import os
from lib.file_io import write_file, append_file, read_file

def test_write_file():
    """Test write_file()"""
    file_name = 'testfile'
    file_content = 'This is a test content.'
    write_file(file_name, file_content)
    assert read_file(file_name) == file_content

def test_append_file():
    """Test append_file()"""
    file_name = 'testfile'
    file_content = 'This is a test content.'
    append_content = 'Appended content.'
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(file_name + '.txt', 'r') as f:
        file_content_read = f.read()
    # Ensure the test matches the function's actual behavior
    assert file_content_read == file_content + append_content

def test_read_file():
    """Test read_file()"""
    file_name = 'testfile'
    file_content = 'Another test content.'
    write_file(file_name, file_content)
    assert read_file(file_name) == file_content
