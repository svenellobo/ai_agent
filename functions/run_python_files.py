import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.basename(abs_file_path).endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", abs_file_path], cwd=abs_work_dir,capture_output=True, text=True, timeout=30)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_files = types.FunctionDeclaration(
    name="run_python_files",
    description="Checks if provided file path leads to a python file and if it does, tries to run it using subprocess. It returns stdout, stderr and return code information if available",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file, relative to the working dictionary, that will be run in a subprocess.",
            ),
        },
    ),
)
