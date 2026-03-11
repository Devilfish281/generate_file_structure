# src/generate_file_structure/generate_file.py


import io
import os
import re
import sys
import tokenize
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter

# from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
# from langchain_community.document_loaders import TextLoader

# Set of directories to exclude from the file structure
EXCLUDED_DIRS = {
    "__pycache__",
    ".git",
    "venv",
    "node_modules",
    "file_structure",
    "build",
    "db",
    "docs",
    "icons",
    "tests",
    "source",
    ".venv",
}


def read_custom_header(script_dir):
    """
    Reads the custom_header.txt file if it exists. Otherwise, returns the default header.

    :param script_dir: Path object of the script's directory.
    :type script_dir: Path
    :return: Header string.
    :rtype: str
    """
    custom_header_path = script_dir / "custom_header.txt"
    default_header = """\
Developer: Developer: # Project Title
- asset_processing_service1

# About the Project
- This project is an Asset Processing Service built with Python, utilizing LangChain and LangGraph for AI capabilities. It processes various types of assets (text, audio, video) and extracts content for use in a knowledge graph.
- “job-driven ToDo/memory agent.”

- This repo is a background worker service, not a user-facing app. Its active runtime in main.py polls Postgres for rows in asset_processing_jobs, pushes eligible jobs onto an asyncio queue, runs worker tasks, updates heartbeats, and handles stuck jobs / retry limits.

-   The current job payload is basically a chat request: each job has thread_id, user_id, todo_kind, message, status fields, and room for the assistant’s last reply in the same table. That schema and the DB helpers live in api_client.py and models.py.

-   What the workers actually do now is in job_processor.py: they invoke a LangGraph-based assistant against the job’s message, using thread_id, user_id,   and todo_kind as graph config, then write the final assistant message back onto the job row. The graph itself is defined in life_goals_agent.py. It is a memory-backed ToDo assistant that maintains:
  -- a user profile
  -- a ToDo collection
  -- user instructions/preferences for how ToDos should be managed

 -   Short-term graph checkpointing is stored in Redis via RedisSaver, and long-term memory is stored in Postgres via PostgresStore. OpenAI is the LLM   backend, initialized through setup_config.py and the utils under my_utils.




# Role and Objective
- Serve as a Python developer working on the 'Asset Processing Service' using modern Python tooling and best practices.
- **Programming language:** Python (already installed).
- **Manages virtual environments:** Poetry (already installed).
- **Package installer for Python:** Poetry.
- **Operating System:** Windows 11.
- **Framework:** LangChain, LangGraph.

# Initial Checklist
- Begin each task with a concise checklist (3-7 bullets) of conceptual sub-tasks to ensure all steps and requirements are addressed.

# Instructions
- Use Visual Studio Code on Windows 11 to develop in Python.
- Manage packages and virtual environments with Poetry.
- Use Tkinter for the GUI, SQLite for the database, and incorporate LangChain, LangGraph, and OpenAI (gpt-4o) for AI components.
- Employ Git and GitHub for version control.
- Use Sphinx for documentation generation.
- **Check my code for errors and suggest improvements.**

## Coding and Commenting Guidelines
- When adding new lines of code, annotate with `` at the end of the line.
- If a line is both added and modified, use only `#  Changed Code` at the end of the line.
- Do **not** comment on command-line instructions.
- Provide complete code context when submitting changes.
- When editing code:
  1. Clearly state any relevant assumptions.
  2. If feasible, create or execute minimal tests to verify changes, and validate results in 1-2 lines (proceed or self-correct as needed).
  3. Provide review-ready diffs.
  4. Follow the established project style conventions.
- **Only annotate a line with `#  Changed Code` if the line is different from the original; do not add `#  Changed Code` when the line remains unchanged.**

# Context
- **Project Directory:** C:/Users/ME/Documents/fullstack/Projects/asset_processing_service
- **GitHub Repository:** https://github.com/Devilfish281/asset_processing_service.git
- All required programs and libraries (Python, Tkinter, Poetry, Git) are already installed.

# Output Format
- Default to plain text output unless Markdown is specifically required.
- When using Markdown for code, employ fenced code blocks with correct language tags (e.g., ```python).
- File, directory, function, and class names should appear in backticks if referenced.
- Escape math notation if present.

# Verbosity
- Use concise summaries for general output.
- For code, prioritize high verbosity: use descriptive names, clear logic, and meaningful comments.

# Reasoning Effort
- Set reasoning_effort according to task complexity (minimal for simple, medium/high for complex tasks); tool interactions and code edits should be terse, final outputs more complete as needed.

# Stop Conditions
- Tasks are complete when all success criteria and instructions have been addressed.
- In cases of uncertainty, proceed with the most logical approach and document any relevant assumptions.
- Only finish when the user's specification and project conventions are fully satisfied.

********************************
Check my code for errors and improvements.

"""
    if custom_header_path.exists():
        try:
            with custom_header_path.open("r", encoding="utf-8") as header_file:
                header = header_file.read()
            print(f"Custom header loaded from '{custom_header_path}'.")
            return header
        except IOError as e:
            print(
                f"Error reading custom header from '{custom_header_path}': {e}",
                file=sys.stderr,
            )
            print("Using default header.")
            return default_header
    else:
        print("Custom header file 'custom_header.txt' not found. Using default header.")
        return default_header


def validate_start_path(start_path: Path) -> Path:
    """Validate the command-line start path and return the resolved directory path."""
    resolved_path = start_path.expanduser().resolve()
    if not resolved_path.exists():
        raise ValueError(f"Start path does not exist: {resolved_path}")
    if not resolved_path.is_dir():
        raise ValueError(f"Start path is not a directory: {resolved_path}")
    return resolved_path


def generate_file_structure(
    root_dir, script_path, output_file, include_tests: bool = False
):  # Changed Code
    """
    Generates the directory structure of the given root directory and collects .py files.

    :param root_dir: The root directory to generate the file structure from.
    :type root_dir: Path
    :param script_path: The path to the running script to exclude from the file structure.
    :type script_path: Path
    :param output_file: The path to the output file to exclude from the file structure.
    :type output_file: Path
    :param include_tests: If True, the 'tests' directory will be included without prompting.
    :type include_tests: bool
    :return: Tuple containing list of directory structure lines and list of .py file paths.
    :rtype: tuple[list[str], list[Path]]
    """
    lines = ["The File structure for my program is BELOW:\n"]
    py_files = []

    # Initial prompt to include all directories
    while True:
        include_all_response = (
            input("Do you want to include all directories? (y/n): ").strip().lower()
        )
        if include_all_response in {"y", "n"}:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"

    for root, dirs, files in os.walk(root_dir):  # Changed Code
        # Convert to Path object for easier manipulation
        root_path = Path(root)

        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        if not include_all:
            # Iterate over a copy of dirs to modify dirs in place  #Added Code
            for d in dirs[:]:  # Added Code
                if d == "tests" and include_tests:
                    continue  # skip per-dir prompt for tests when user opted in
                while True:
                    response = (
                        input(f"Do you want to include the directory '{d}'? (y/n): ")
                        .strip()
                        .lower()
                    )
                    if response in {"y", "n"}:
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                if response == "n":
                    dirs.remove(d)
                    EXCLUDED_DIRS.add(d)
                    print(f"Excluded directory: {d}")

        # Compute the level by relative parts
        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            # In case root_path is same as root_dir
            level = 0

        indent = "    " * level

        # Get directory name
        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        # Determine branch symbol
        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        # Prepare indentation for files
        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "    "
        else:
            sub_indent = indent + "│   "

        # Sort files for consistent ordering
        files = sorted(files)
        for idx, f in enumerate(files):
            # Exclude the running script and the output file
            file_path = root_path / f
            if (
                file_path.resolve() == script_path.resolve()
                or file_path.resolve() == output_file.resolve()
            ):
                continue

            # Collect .py files for later processing
            if f.endswith(".py"):
                py_files.append(file_path)

            file_branch = "└── " if idx == len(files) - 1 else "├── "
            lines.append(f"{sub_indent}{file_branch}{f}\n")

    return lines, py_files


def is_last_item(root_path, dirs, files):
    """
    Determines if the current directory is the last item in its parent directory.

    :param root_path: Path object of the current directory.
    :param dirs: List of subdirectories.
    :param files: List of files.
    :return: Boolean indicating if it's the last item.
    """
    parent = root_path.parent
    siblings = [
        s for s in parent.iterdir() if s.is_dir() and s.name not in EXCLUDED_DIRS
    ]
    sorted_siblings = sorted(siblings, key=lambda s: s.name)
    return root_path == sorted_siblings[-1] if siblings else False


def create_chat_gpt_directory(output_file):
    """
    Creates the 'chat_gpt' directory and prepares the output file path.

    :param output_file: The path to the output file.
    :type output_file: Path
    """
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{output_file.parent}' is ready.")
    except IOError as e:
        print(
            f"An error occurred while creating '{output_file.parent}': {e}",
            file=sys.stderr,
        )
        sys.exit(1)


###############################################################################
# Code Cleaning Section
###############################################################################
def remove_comments_from_code(source_code: str) -> str:
    """
    Removes all comments from the provided Python source code without altering the original formatting.

    :param source_code: The original Python source code as a string.
    :type source_code: str
    :return: The source code without any comments.
    :rtype: str
    """

    # Compile a regular expression pattern for comment-like text.
    # In this function, the compiled pattern is not actually used later.
    comment_pattern = re.compile(r"(?<!:)#.*")

    ###########################################################################
    # The above regex matches any '#' character that is not preceded by a colon
    # (to avoid matching shebang lines like '#!/usr/bin/env python').
    # It captures the '#' and everything that follows it on the same line,
    # effectively matching comments while ignoring '#' characters
    # that are part of strings or other code constructs.
    ###########################################################################
    def remove_inline_comment(line: str) -> str:
        """
        Removes inline comments from a single line of code.

        :param line: A single line of Python code.
        :type line: str
        :return: The line without comments.
        :rtype: str
        """
        # Track whether the current position is inside a single-quoted string.
        in_single_quote = False

        # Track whether the current position is inside a double-quoted string.
        in_double_quote = False

        # Track whether the previous character was a backslash escape.
        escape = False

        # Walk through the line one character at a time so we can detect
        # whether a '#' is part of real code or part of a string literal.
        for i, char in enumerate(line):
            # If we see a backslash and we are not already in escape mode,
            # mark the next character as escaped and continue.
            if char == "\\" and not escape:
                escape = True
                continue

            # Only update quote state when the current character is not escaped.
            if not escape:
                # Toggle single-quote mode if we hit a single quote while not
                # already inside a double-quoted string.
                if char == "'" and not in_double_quote:
                    in_single_quote = not in_single_quote

                # Toggle double-quote mode if we hit a double quote while not
                # already inside a single-quoted string.
                elif char == '"' and not in_single_quote:
                    in_double_quote = not in_double_quote

                # If we find a '#' while not inside any quoted string,
                # treat it as the start of a comment and keep only the code
                # before it. `rstrip()` removes trailing whitespace.
                elif char == "#" and not in_single_quote and not in_double_quote:
                    return line[:i].rstrip()

            # Reset escape mode after processing the current character.
            escape = False

        # If no real comment marker was found, return the whole line with
        # trailing whitespace removed. `rstrip()` removes trailing whitespace.
        return line.rstrip()

    #############################################################################
    # The helper above uses manual character scanning instead of the regex
    # pattern so it can avoid removing '#' characters that appear inside
    # quoted strings.
    #############################################################################

    # Store the cleaned result one line at a time.
    cleaned_lines = []

    # `splitlines()` breaks the input source into individual lines for processing.
    for line in source_code.splitlines():
        # Remove leading and trailing whitespace only for the purpose of checking
        # whether the entire line is just a comment.
        stripped_line = line.strip()

        # Skip full-line comments such as:
        #     # this is a comment
        if stripped_line.startswith("#"):
            continue
        else:
            # For non-comment lines, remove only the inline comment part.
            cleaned_line = remove_inline_comment(line)
            cleaned_lines.append(cleaned_line)

    # Join the cleaned lines back together into one string separated by newlines.
    return "\n".join(cleaned_lines)


################################################################################
# File Appending Section
################################################################################
def append_file_contents(output_file, py_files):
    """
    Appends the contents of each .py file to the output file with a header and enhances readability.
    Preserves the first line of the file and removes all comments from the rest of the code.

    Python file in py_files, it:
        writes a separator/header,
        starts a Markdown code block,
        reads the Python file,
        keeps the first line,
        removes comments from the rest of the file,
        writes the cleaned code into the output file,
        then closes the Markdown code block.

    :param output_file: The path to the output file.
    :type output_file: Path
    :param py_files: List of paths to .py files.
    :type py_files: list[Path]
    """
    try:
        # Append to the output file instead of overwriting
        with output_file.open("a", encoding="utf-8") as file:
            # Iterate over each Python file and append its contents with a header and separators
            for py_file in py_files:
                # write the code header and separators for readability
                separator = "########################################"
                # Write the first separator and header
                file.write(f"\n{separator}\n")
                file.write(f"Here is my code for {py_file.name} BELOW:\n")
                # Write the second separator
                file.write(f"{separator}\n\n")
                # Start of Markdown code block
                file.write(f"```python\n")

                try:
                    with py_file.open("r", encoding="utf-8") as py_f:
                        source_code = py_f.read()
                        if not source_code:
                            cleaned_code = ""
                        else:
                            lines = source_code.splitlines()
                            first_line = lines[0]
                            rest_of_code = "\n".join(lines[1:])
                            # Remove all comments from the rest of the code
                            cleaned_rest = remove_comments_from_code(rest_of_code)
                            # Ensure the first line ends with a newline
                            if not first_line.endswith("\n"):
                                first_line += "\n"
                            cleaned_code = first_line + cleaned_rest

                        if cleaned_code and not cleaned_code.endswith(
                            "\n"
                        ):  # Added Code
                            cleaned_code += "\n"  # Added Code

                        file.write(cleaned_code)
                except UnicodeDecodeError:
                    file.write(
                        f"# Could not decode file {py_file} with UTF-8 encoding.\n\n"
                    )
                except IOError as e:
                    file.write(f"# Could not read file {py_file}: {e}\n\n")
                # Close the Markdown code fence on its own line
                file.write(f"```\n")
        print(f"Python file contents appended to '{output_file}'.")
    except IOError as e:
        print(
            f"An error occurred while appending to '{output_file}': {e}",
            file=sys.stderr,
        )


def add_custom_header(output_file, script_dir):
    """
    Adds a custom header to the top of the output file. Reads from 'custom_header.txt' if it exists,
    otherwise uses the default header.

    :param output_file: The path to the output file.
    :type output_file: Path
    :param script_dir: Path object of the script's directory.
    :type script_dir: Path
    """
    header = read_custom_header(script_dir)
    try:
        with output_file.open("w", encoding="utf-8") as file:
            file.write(header + "\n\n")
        print(f"Header written to '{output_file}'.")
    except IOError as e:
        print(
            f"An error occurred while writing header to '{output_file}': {e}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> tuple[Path, Path]:  # Changed Code
    """
    Entry point of the script. Allows optional command-line arguments for root directory and output file.
    Excludes the script itself and the output directory from the file structure.
    Appends the contents of each .py file after the directory structure.
    Adds a custom header to the top of the output file.
    Enhances readability by adding separators.

    :return: The resolved output file path created by the program.
    :rtype: Path
    """
    import argparse

    # Determine the script's directory
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent

    parser = argparse.ArgumentParser(
        description=(
            "Generate a comprehensive report of your Python project's directory structure and code.\n\n"
            "This script scans the specified start path, excluding certain directories and files, "
            "and generates an output file containing the directory structure and the contents of each Python file. "
            "Users can customize the header of the output file by providing a 'custom_header.txt' file in the script's directory.\n\n"
            "Instructions:\n"
            "- If 'custom_header.txt' exists, its contents will be used as the header.\n"
            "- If not, a default header will be used.\n\n"
            "Usage Examples:\n"
            "  python generate_file_structure.py --start-path C:\\Users\\ME\\Documents\\Python\\2026\\langchain-academy\n"
            "  python generate_file_structure.py --start-path C:\\Users\\ME\\Documents\\Python\\2026\\langchain-academy --output C:\\temp\\output.txt"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-s",
        "--start-path",
        type=Path,
        default=script_dir.parent,
        help=(
            f"Starting directory to scan (default: parent of script's directory: {script_dir.parent})\n"
            "Example: --start-path C:\\Users\\ME\\Documents\\Python\\2026\\langchain-academy"
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,  # Changed Code
        help=(  # Changed Code
            "Output file path (default: <start-path>/chat_gpt/program_chat_gpt.txt)\n"  # Changed Code
            "Example: --output C:\\Users\\ME\\Documents\\Python\\2026\\Projects\\test_program_file_structure\\chat_gpt\\program_chat_gpt.txt"  # Changed Code
        ),
    )

    args = parser.parse_args()

    try:
        start_path = validate_start_path(args.start_path)
    except ValueError as e:
        print(f"Invalid start path: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output is None:  # Added Code
        output_path = (
            start_path / "chat_gpt" / "program_chat_gpt.txt"
        ).resolve()  # Added Code
    else:  # Added Code
        output_path = args.output.expanduser().resolve()  # Added Code

    print(f"Scanning start path: '{start_path}'")
    print(f"Using output file: '{output_path}'")

    # === Ask whether to include tests directory (y/n) ===
    include_tests = False
    try:
        while True:
            resp = (
                input("Do you want to include tests directory? (y/n): ").strip().lower()
            )
            if resp in {"y", "n"}:
                include_tests = resp == "y"
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    except EOFError:
        include_tests = False

    if include_tests and "tests" in EXCLUDED_DIRS:
        EXCLUDED_DIRS.remove("tests")

    # Exclude the output directory by adding its name to EXCLUDED_DIRS
    EXCLUDED_DIRS.add(output_path.parent.name)

    # Create the output directory if it doesn't exist
    create_chat_gpt_directory(output_path)

    # Add custom header to the output file
    add_custom_header(output_path, script_dir)

    # print information about the scanning process
    print("\n--- Starting to Generate the file structure ---")
    print("\n--- Scan Configuration ---")
    print(f"Scanning start path: '{start_path}'")
    print(f"Excluding script: '{script_path}'")
    print(f"Using output file: '{output_path}'")
    print(f"Including 'tests' directory: {'Yes' if include_tests else 'No'}")

    # Generate the file structure and collect .py files
    structure_lines, py_files = generate_file_structure(
        start_path,
        script_path,
        output_path,
        include_tests=include_tests,
    )

    # Append the directory Tree structure to the output file after the header
    try:
        with output_path.open("a", encoding="utf-8") as file:
            file.writelines(structure_lines)
        print(f"File structure appended to '{output_path}'.")
    except IOError as e:
        print(
            f"An error occurred while appending directory structure to '{output_path}': {e}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Append the contents of each .py file
    if py_files:
        append_file_contents(output_path, py_files)
    else:
        print("No Python files found to append.")

    # If tests were requested, also include pytest.ini content in the output
    if include_tests:
        pytest_ini_path = start_path / "pytest.ini"
        try:
            if pytest_ini_path.exists():
                with output_path.open("a", encoding="utf-8") as file:
                    separator = "########################################"
                    file.write(f"\n{separator}\n")
                    file.write("Here is my pytest.ini BELOW:\n")
                    file.write(f"{separator}\n\n")
                    file.write("```ini\n")
                    file.write(pytest_ini_path.read_text(encoding="utf-8"))
                    file.write("\n```\n")
                print(f"pytest.ini appended to '{output_path}'.")
            else:
                print("pytest.ini not found; skipping append.")
        except Exception as e:
            print(f"Failed to append pytest.ini: {e}", file=sys.stderr)

    return output_path, start_path  # Changed Code


###################################################################################
# RAG (Retrieval-Augmented Generation) Section
###################################################################################
def rag_text(output_file: Path, start_path: Path) -> None:  # Changed Code
    import shutil  # Ensure shutil is imported within the function or at the top of the script

    # Always keep generated support folders beside this script.
    script_dir = Path(__file__).resolve().parent

    # Resolve the actual report file path.
    output_file = output_file.expanduser().resolve()
    start_path = start_path.expanduser().resolve()  # Added Code

    # Force chunk output into the source folder, not the scanned project.
    chunks_dir = start_path / "chat_gpt" / "chunks"  # Changed Code
    db_dir = start_path / "chat_gpt" / "db"  # Changed Code
    db_dir.mkdir(parents=True, exist_ok=True)  # Changed Code

    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # persistent_directory = os.path.join(current_dir, "db", "rag_chroma_db")
    # os.makedirs(os.path.join(current_dir, "db"), exist_ok=True)
    # file_path = os.path.join(current_dir, "chat_gpt", "program_chat_gpt.txt")
    # chunks_dir = os.path.join(current_dir, "chat_gpt", "chunks")

    if chunks_dir.exists():
        try:
            shutil.rmtree(chunks_dir)
            print(f"Existing 'chunks' directory '{chunks_dir}' has been removed.")
        except Exception as e:
            print(
                f"Error removing 'chunks' directory '{chunks_dir}': {e}",
                file=sys.stderr,
            )
            sys.exit(1)
    # Create the chunks directory if it doesn't exist
    try:
        chunks_dir.mkdir(parents=True, exist_ok=True)
        print(f"'chunks' directory '{chunks_dir}' has been created.")
    except Exception as e:
        print(f"Error creating 'chunks' directory '{chunks_dir}': {e}", file=sys.stderr)
        sys.exit(1)

    # Check if the Chroma vector store already exists
    # if not os.path.exists(persistent_directory):
    print("Preparing generated report for token-based chunking...")  # Changed Code

    # Ensure the text file exists
    if not output_file.exists():
        raise FileNotFoundError(
            f"The file {output_file} does not exist. Please check the path."
        )

    try:
        loader = TextLoader(
            str(output_file), encoding="utf-8", autodetect_encoding=True
        )
        documents = loader.load()
    except UnicodeDecodeError as e:
        # If autdetect failed, try again with latin-1 then raise
        try:
            loader = TextLoader(
                str(output_file), encoding="latin-1", autodetect_encoding=False
            )
            documents = loader.load()
        except Exception as e2:
            print(f"Unicode decoding failed: {e} and fallback failed: {e2}")
            sys.exit(1)

    # Remove or replace any model special-token markers (like "") from text.
    SPECIAL_TOKENS_TO_STRIP = [
        "<|endoftext|>",
        "<|im_start|>",
        "<|im_end|>",
    ]
    for doc in documents:
        if any(tok in doc.page_content for tok in SPECIAL_TOKENS_TO_STRIP):
            for tok in SPECIAL_TOKENS_TO_STRIP:
                if tok in doc.page_content:
                    doc.page_content = doc.page_content.replace(tok, "")
    # --- END: sanitize special tokens ---

    print("\n--- Using Token-based Splitting ---")
    # Use explicit tokenizer config; disallowed_special=() disables strict checks and treats special-token text as normal text.
    token_splitter = TokenTextSplitter(
        chunk_overlap=100,
        chunk_size=32000,
        encoding_name="cl100k_base",  #  (explicit encoding; adjust if you want a different encoding)
        disallowed_special=(),  #  (disables the check so special tokens won't raise ValueError)
    )
    docs = token_splitter.split_documents(documents)

    # Split the document into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=30000, chunk_overlap=0)
    # docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    if docs:
        print(f"Sample chunk:\n{docs[0].page_content}\n")
    else:
        print("No chunks were generated.\n")

    # Write each chunk to a separate file
    for idx, doc in enumerate(docs, start=1):
        chunk_filename = f"chunk{idx}.txt"
        chunk_path = chunks_dir / chunk_filename
        try:
            with chunk_path.open("w", encoding="utf-8") as chunk_file:
                chunk_file.write(doc.page_content)
            print(f"Written {chunk_filename}")
        except IOError as e:
            print(f"Failed to write {chunk_filename}: {e}")

    print("RAG DONE! Chunks have been written to the 'chunks' directory.")
    print("RAG DONE! DB directory is under 'chat_gpt/db'.")  # Added Code


if __name__ == "__main__":
    generated_output_file, start_path = main()  # Changed Code
    rag_text(generated_output_file, start_path)  # Changed Code
    print("Program DONE!.")
