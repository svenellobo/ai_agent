import os

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



    """try:
        working_path = Path(working_directory).resolve()

        if directory:
            directory_path = Path(directory).resolve()

            # Check if directory is outside working_path
            try:
                directory_path.relative_to(working_path)
            except ValueError:
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            directory_path = working_path

        if not directory_path.is_dir():
            target = directory if directory is not None else str(directory_path)
            return f'Error: "{target}" is not a directory'

        results = []
        for item in directory_path.iterdir():
            results.append(f"- {item.name}: file_size={item.stat().st_size} bytes, is_dir={item.is_dir()}")

        return "\n".join(results)

    except Exception as e:
        return f"Error: {str(e)}" """