import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

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
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()

