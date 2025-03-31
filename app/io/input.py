import pandas as pd
def input_from_console():
    """
    Function to input text from console.
    
    Returns:
        str: Text input from console
    """
    text = input("Enter your text: ")
    return text


def read_from_file_builtin(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: Content of the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def read_from_file_pandas(file_path):
    """
    Function to read data from a file using pandas library.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        pandas.DataFrame: Data read from the file
    """

        
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
            data = pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        data = pd.read_json(file_path)
    else:
            data = pd.read_csv(file_path)
            
    return data
