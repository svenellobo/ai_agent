import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        full_wd_path = os.path.abspath(working_directory)
        
        if not directory:
            directory = "."
        joined_directory = os.path.join(working_directory, directory)
        full_dir_path = os.path.abspath(joined_directory)
        
        if not full_dir_path.startswith(full_wd_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_dir_path):
            return f'Error: "{directory}" is not a directory'
        
        results = []    
        for item in os.listdir(full_dir_path):
            results.append(f"- {item}: file_size={os.path.getsize(os.path.join(full_dir_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_dir_path, item))}")
            
        return "\n".join(results)
    
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)