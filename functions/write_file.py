import os

def write_file(working_directory, file_path, content):
    full_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    dir_name = os.path.dirname(full_directory)
    if not os.path.isdir(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            return f"Error: Could not create directory: {e}"
    try:
        with open(full_directory, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Could not write to file: {e}"