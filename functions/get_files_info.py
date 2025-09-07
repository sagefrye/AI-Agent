import os
def get_files_info(working_directory, directory="."):
    full_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.isdir(full_directory):
        return f'Error: "{directory}" is not a directory'
    if not full_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        contents = os.listdir(full_directory)
        return_list = []
        for item in contents:
            item_path = os.path.join(full_directory, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            return_list.append(f"- {item}: file_size={file_size} bytes, is_dir={str(is_dir)}")
        return_str = "\n".join(return_list)
        return return_str
    except Exception as e:
        return f"Error listing files: {e}"