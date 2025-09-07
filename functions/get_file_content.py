import os

def get_file_content(working_directory, file_path):
    full_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        max_chars = 10000
        with open(full_directory, "r") as f:
            file_content_string = f.read(max_chars)
            if os.path.getsize(full_directory) > max_chars:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {max_chars} characters]'
                )
        return file_content_string
    except Exception as e:
        return f'Error: Could not read file "{file_path}": {e}'