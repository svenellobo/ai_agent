import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from prompts import system_prompt
from call_function import available_functions, call_function


def main():    
    load_dotenv()


    verbose = "--verbose" in sys.argv
    arguments = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not arguments:
        print("Error: invalid input", file=sys.stderr)
        sys.exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    full_prompt = " ".join(arguments)

    

    if verbose:
        print(f"User prompt: {full_prompt}\n")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=full_prompt)]),
    ]  

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    for i in range(20):

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
        )
        
        responses_list = response.candidates
        for r in responses_list:
            messages.append(r.content)


        if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)
        
            
        if response.function_calls:
            for f in response.function_calls:
                func_value = call_function(f)
                messages.append(func_value)
                if not func_value.parts[0].function_response.response:
                    raise Exception("Fatal exception: something went wrong")
                elif func_value.parts[0].function_response.response and verbose:                
                    print(f"-> {func_value.parts[0].function_response.response}")

        
                
        else:       

            print("Response:")
            print(response.text)
            break
    

if __name__ == "__main__":
    main()

