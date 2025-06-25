# AI Coding Agent

This project implements an AI-powered coding agent that can analyze, execute, and modify code in a target Python project (such as the included calculator app). The agent leverages Google's Gemini API to interpret user prompts and perform actions like listing files, reading file contents, running Python scripts, and writing files, all within a secure working directory.

## Features

- **Natural Language Interface:** Interact with the agent using plain English prompts.
- **File Operations:** List files, read file contents, and write or overwrite files within the working directory.
- **Code Execution:** Run Python scripts and capture their output and errors.
- **Security:** All file operations are sandboxed to the specified working directory.
- **Extensible Functions:** Easily add new capabilities by defining new function schemas and implementations.

## Project Structure

- [`main.py`](main.py): Entry point for the AI agent. Handles prompt input, Gemini API interaction, and function call orchestration.
- [`call_function.py`](call_function.py): Maps function calls from the AI model to actual Python implementations.
- [`prompts.py`](prompts.py): Contains the system prompt for the AI agent.
- [`functions/`](functions/): Implements file and execution operations:
  - [`get_files_info.py`](functions/get_files_info.py): List files and directories.
  - [`get_file_content.py`](functions/get_file_content.py): Read file contents.
  - [`run_python_files.py`](functions/run_python_files.py): Execute Python files.
  - [`write_file.py`](functions/write_file.py): Write or overwrite files.
- [`calculator/`](calculator/): Example target project (a simple calculator app with tests).
- [`tests.py`](tests.py): Test script for the agent's function implementations.

## Getting Started

### Prerequisites

- Python 3.8+
- [Google Gemini API key](https://ai.google.dev/)
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### Setup

1. Create a `.env` file in the project root with your Gemini API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

2. Run the agent:
    ```sh
    python main.py "Analyze calculator app and suggest improvements"
    ```

    Add `--verbose` for detailed output.

### Example Usage

- **Analyze the calculator app:**
  ```sh
  python main.py "Analyze calculator app and suggest improvements"
  ```
- **Read a file:**
  ```sh
  python main.py "Show me the contents of calculator/pkg/calculator.py"
  ```
- **Run tests:**
  ```sh
  python main.py "Run the tests in calculator/tests.py"
  ```

## Security

All file operations are restricted to the working directory (by default, `./calculator`). Attempts to access files outside this directory are blocked.

## Extending

To add new capabilities, define a new function and schema in the `functions/` directory, then register it in [`call_function.py`](call_function.py).



---

*This project is for educational and research purposes. Use responsibly and ensure you comply with the terms of the Gemini API and any other dependencies.*