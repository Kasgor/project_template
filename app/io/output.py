def output_to_console(text):
    """
    Function to output text to console.
    
    Args:
        text: The text or data to output
    """
    print(text)


def write_to_file_builtin(file_path, content):
    """
    Function to write content to a file using Python's built-in capabilities.
    
    Args:
        file_path (str): Path to the file to write
        content (str): Content to write to the file
        
    Returns:
        bool: True if writing was successful, False otherwise
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def append_to_file_builtin(file_path, content):
    """
    Function to append content to a file using Python's built-in capabilities.
    
    Args:
        file_path (str): Path to the file to append to
        content (str): Content to append to the file
        
    Returns:
        bool: True if appending was successful, False otherwise
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False