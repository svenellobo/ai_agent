import os

def get_file_content(working_directory, file_path):
    
    full_wd_path = os.path.abspath(working_directory)


    if not file_path:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    
    joined_path = os.path.join(working_directory, file_path)            
    full_path = os.path.abspath(joined_path)
        

    if not full_path.startswith(full_wd_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
        
    try:
        MAX_CHARS = 10000
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1) != "":
                return file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'

            return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"