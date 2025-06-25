from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_files  import schema_run_python_files, run_python_file
from functions.write_file import schema_write_file, write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_files
    ]
)

function_map = {
    "get_files_info":get_files_info,
    "get_file_content":get_file_content,
    "write_file":write_file,
    "run_python_file":run_python_file
}

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_call_part.name in function_map:
        args_dict_copy = function_call_part.args.copy()
        args_dict_copy["working_directory"] = "./calculator"
        result = function_map[function_call_part.name](**args_dict_copy)

    else:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result},
            )
        ],
    )
