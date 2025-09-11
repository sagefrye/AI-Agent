import os
from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content to a specified file, constrained to the working directory. If the file path does not exist, a new file is created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to retrieve the content from, reletave to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file."
            )
        },
    ),
)