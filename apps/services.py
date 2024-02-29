import ast
import math
import resource
import subprocess


# def bytes_to_human_readable(bytes_value):
#     kb_value = bytes_value / 1024
#     return f"{math.ceil(kb_value)} KB"

# Update your existing run_python_code function
def run_python_code(python_code, timeout):
    try:
        with open('temp.py', 'w') as file:
            file.write(python_code)
            file.write('\n')  # Add a newline for separation
        process = subprocess.Popen(['/home/nusratullo/pycharm/python_tutorials/venv/bin/python', 'temp.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(timeout=timeout)

        return output, error

    except subprocess.TimeoutExpired:
        raise TimeoutError("Execution time exceeded, action stopped.")

def get_actual_type(data_str):
    try:
        value = ast.literal_eval(data_str)
        actual_type = type(value).__name__
    except (ValueError, SyntaxError):
        value = str(data_str)
        actual_type = "invalid"
    return value, actual_type
