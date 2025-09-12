import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_directory):
        return f'Error: File "{file_path}" not found.'
    if not full_directory.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    commands = ["uv", "run", full_directory] + args
    try:
        result = subprocess.run(commands, timeout=30, capture_output=True, cwd=os.path.abspath(working_directory))
        return_string = [f"STDOUT: {result.stdout}", f"STDERR: {result.stderr}"]
        if result.returncode != 0:
            return_string.append(result.returncode)
        if not result:
            return "No output produced"
        return "\n".join(return_string)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python script with the given arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the Python script, reletave to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="The arguments needed for the Python script"
                ),
                description="The arguments needed for the Python script."
            )
        },
        required=["file_path"]
    ),
)
    