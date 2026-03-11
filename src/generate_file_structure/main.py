# src/generate_file_structure/main.py
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# RAG imports
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter

from generate_file_structure.my_utils.directory_setup import (
    create_chat_gpt_directory_once,
)
from generate_file_structure.my_utils.env_loader import load_dotenv_once
from generate_file_structure.my_utils.path_utils import validate_path
from generate_file_structure.setup_config import c_setup_config

load_dotenv_once()
# from asset_processing_service.config import config
setup_config = c_setup_config.get_instance()
logger = setup_config.get_logger()


# Set of directories to exclude from the file structure
EXCLUDED_PYTHON_DIRS = {
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
# -- Included --
INCLUDED_PYTHON_FILES = {
    ".py",
    ".toml",
}
INCLUDED_PYTHON_TEST_FILES = {
    ".ini",
}
###################################################################################
# Next.js specific settings
# for nextjs typescript tailwind shadcn
###################################################################################
EXCLUDED_NEXTJS_DIRS = {
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
    ".next",
    "out",
    "coverage",
}

INCLUDED_NEXTJS_FILES = {
    ".tsx",
    ".ts",
    ".css",
    ".json",
    ".md",
    ".mdx",
}

INCLUDED_NEXTJS_TEST_FILES = {
    ".ini",
}
"""
The combination of Next.js, TypeScript, Tailwind CSS, and shadcn/ui is a
popular modern stack for building robust, type-safe, and visually appealing
web applications. This stack leverages the strengths of each technology to
provide a streamlined developer experience.

Key Components

Next.js
A React framework for building full-stack web applications. It supports
server-side rendering (SSR), static site generation (SSG), and API routes.

TypeScript
A superset of JavaScript that adds static typing, reducing runtime errors
and improving code maintainability and developer productivity.

Tailwind CSS
A utility-first CSS framework that lets you style applications directly in
markup using small, composable utility classes.

shadcn/ui
A collection of reusable UI components built with Radix UI and styled with
Tailwind CSS. Instead of a packaged UI library, you copy the component
source code into your project, giving full customization and ownership.
"""


def create_program_excluded():
    """
    Creates the 'chat_gpt' directory and prepares the output file path.

    :type output_dir: Path
    """
    try:

        ###########################################################################
        # Test inclusion settings
        ###########################################################################
        if setup_config.get_project_type() == "python":
            if not setup_config.include_tests_flag and "tests" in EXCLUDED_PYTHON_DIRS:
                EXCLUDED_PYTHON_DIRS.remove("tests")

        if setup_config.get_project_type() == "next_js":
            if not setup_config.include_tests_flag and "tests" in EXCLUDED_NEXTJS_DIRS:
                EXCLUDED_NEXTJS_DIRS.remove("tests")

        # Exclude the output directory by adding its name to EXCLUDED_DIRS
        main_dir = setup_config.get_program_output_dir()
        EXCLUDED_PYTHON_DIRS.add(main_dir.name)
        EXCLUDED_NEXTJS_DIRS.add(main_dir.name)

        logger.info(f"Directory '{main_dir}' is ready.")
    except ValueError as e:
        logger.error(f"An error occurred while creating '{main_dir}': {e}")
        sys.exit(1)


def read_custom_header_beginning():
    custom_header_location = setup_config.output_dir
    project_title_raw = custom_header_location.stem
    project_title = project_title_raw.replace("_", " ").title()

    default_header = f"""\
Developer: Developer: 
# Project Title
- {project_title}
"""

    custom_header_path = setup_config.get_custom_header_beginning_location()
    if custom_header_path.exists():
        try:
            with custom_header_path.open("r", encoding="utf-8") as header_file:
                header = header_file.read()
            logger.info(f"Custom beginning header loaded from '{custom_header_path}'.")
            return header
        except IOError as e:
            logger.error(
                f"Error reading custom beginning header from '{custom_header_path}': {e}"
            )
            logger.info("Using default beginning header.")
            return default_header
    else:
        logger.info(
            f"Custom beginning header file '{setup_config.custom_header_beginning_name}' not found. Using default beginning header."
        )
        return default_header


def read_custom_header():
    """
    Reads the custom_header.txt file if it exists. Otherwise, returns the default header.

    :param script_dir: Path object of the script's directory.
    :type script_dir: Path
    :return: Header string.
    :rtype: str
    """

    default_header = """\

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
- When adding new lines of code, annotate with `#  Added Code` at the end of the line.
- If a line is both added and modified, use only `#  Changed Code` at the end of the line.
- Do **not** comment on command-line instructions.
- Provide complete code context when submitting changes.
- When editing code:
  1. Clearly state any relevant assumptions.
  2. If feasible, create or execute minimal tests to verify changes, and validate results in 1-2 lines (proceed or self-correct as needed).
  3. Provide review-ready diffs.
  4. Follow the established project style conventions.
- **Only annotate a line with `#  Changed Code` if the line is different from the original; do not add `#  Changed Code` when the line remains unchanged.**

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
    custom_header_path = setup_config.get_custom_header_location()
    if custom_header_path.exists():
        try:
            with custom_header_path.open("r", encoding="utf-8") as header_file:
                header = header_file.read()
            logger.info(f"Custom header loaded from '{custom_header_path}'.")
            return header
        except IOError as e:
            logger.error(
                f"Error reading custom header from '{custom_header_path}': {e}"
            )
            logger.info("Using default header.")
            return default_header
    else:
        logger.info(
            f"Custom header file '{setup_config.custom_header_name}' not found. Using default header."
        )
        return default_header


def add_custom_header():
    """
    Adds a custom header to the top of the output file. Reads from 'custom_header.txt' if it exists,
    otherwise uses the default header.

    """
    # Date and time for the header
    header_today_date = "# Today's Date: \n- " + datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    header_beginning = read_custom_header_beginning()
    header = read_custom_header()
    try:
        with setup_config.get_output_file_path().open("w", encoding="utf-8") as file:
            file.write(
                header_today_date + "\n\n" + header_beginning + "\n\n" + header + "\n\n"
            )
        logger.info(f"Header written to '{setup_config.get_output_file_path()}'.")
    except IOError as e:
        logger.error(
            f"An error occurred while writing header to '{setup_config.get_output_file_path()}': {e}"
        )
        sys.exit(1)


def is_last_item(root_path, dirs, files):
    """
    Determines if the current directory is the last item in its parent directory.

    :param root_path: Path object of the current directory.
    :param dirs: List of subdirectories.
    :param files: List of files.
    :return: Boolean indicating if it's the last item.
    """
    parent = root_path.parent

    if setup_config.get_project_type() == "python":
        siblings = [
            s
            for s in parent.iterdir()
            if s.is_dir() and s.name not in EXCLUDED_PYTHON_DIRS
        ]

    if setup_config.get_project_type() == "next_js":
        siblings = [
            s
            for s in parent.iterdir()
            if s.is_dir() and s.name not in EXCLUDED_NEXTJS_DIRS
        ]

    sorted_siblings = sorted(siblings, key=lambda s: s.name)
    return root_path == sorted_siblings[-1] if siblings else False


def generate_file_structure():
    """
    Generates the directory structure of the given root directory and collects .py files.

    :return: Tuple containing list of directory structure lines and list of .py file paths.
    :rtype: tuple[list[str], list[Path]]
    """
    lines = ["The File structure for my program is BELOW:\n"]
    py_files_list = []
    root_dir = setup_config.output_dir
    output_file = setup_config.get_output_file_path()

    logger.info("--- Generate File Tree ---")
    logger.info(f"Scanning start path: '{root_dir}'")
    logger.info(f"Writhing to the Output File  {output_file}")

    if setup_config.get_project_type() == "python":
        excluded_dirs = EXCLUDED_PYTHON_DIRS
        included_file_suffixes = set(INCLUDED_PYTHON_FILES)
        if setup_config.include_tests_flag:
            included_file_suffixes.update(INCLUDED_PYTHON_TEST_FILES)
    else:
        excluded_dirs = EXCLUDED_NEXTJS_DIRS
        included_file_suffixes = set(INCLUDED_NEXTJS_FILES)
        if setup_config.include_tests_flag:
            included_file_suffixes.update(INCLUDED_NEXTJS_TEST_FILES)

    ###########################################################################
    # Initial prompt to include all directories
    ###########################################################################
    while True:
        include_all_response = (
            input("Do you want to include all directories? (y/n): ").strip().lower()
        )
        if include_all_response in {"y", "n"}:
            break
        else:
            logger.info("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"
    ###########################################################################
    # Walk the directory tree
    ###########################################################################
    for root, dirs, files in os.walk(root_dir):
        # Convert to Path object for easier manipulation
        root_path = Path(root)

        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        #######################################################################
        # NOT All Directories - Ask user for each directory
        #######################################################################
        if not include_all:
            filtered_entries = []
            for child in entries:
                if not child.is_dir():
                    filtered_entries.append(child)
                    continue

                if child.name == "tests" and setup_config.include_tests_flag:
                    filtered_entries.append(child)
                    continue

                while True:
                    response = (
                        input(
                            f"Do you want to include the directory '{child.name}'? (y/n): "
                        )
                        .strip()
                        .lower()
                    )
                    if response in {"y", "n"}:
                        break
                    logger.info("Invalid input. Please enter 'y' or 'n'.")

                if response == "y":
                    filtered_entries.append(child)
                else:
                    excluded_dirs.add(child.name)
                    logger.info(f"Excluded directory: {child.name}")

            entries = filtered_entries
        #######################################################################
        # END of loop NOT All Directories
        #######################################################################

        #######################################################################
        # Compute the level by relative parts
        #######################################################################
        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            # In case root_path is same as root_dir
            level = 0

        indent = "│   " * level

        # Get directory name
        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        # Determine branch symbol
        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        # Prepare indentation for files
        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "│   "
        else:
            sub_indent = indent + "│   "

        # Sort files for consistent ordering
        files = sorted(files)

        ###########################################################################
        # Process files in the current directory
        ###########################################################################
        for idx, f in enumerate(files):
            # Exclude the running script and the output file
            file_path = root_path / f
            if file_path.resolve() == output_file.resolve():
                continue

            # Collect included files for later processing
            if file_path.suffix in included_file_suffixes:
                py_files_list.append(file_path)

            file_branch = "└── " if idx == len(files) - 1 else "├── "
            lines.append(f"{sub_indent}{file_branch}{f}\n")

    return lines, py_files_list


def write_directory_tree_to_file(structure_lines):

    # Append the directory structure to the output file after the header
    try:
        with setup_config.get_output_file_path().open("a", encoding="utf-8") as file:
            file.writelines(structure_lines)
        logger.info(
            f"File structure appended to '{setup_config.get_output_file_path()}'."
        )
    except IOError as e:
        logger.error(
            f"An error occurred while appending directory structure to '{setup_config.get_output_file_path()}': {e}"
        )
        sys.exit(1)


###########################################################################
# write files section
###########################################################################
def remove_comments_from_code(source_code: str) -> str:
    """
    Removes all comments from the provided Python source code without altering the original formatting.

    :param source_code: The original Python source code as a string.
    :type source_code: str
    :return: The source code without any comments.
    :rtype: str
    """

    # Regex pattern to match comments
    comment_pattern = re.compile(r"(?<!:)#.*")

    def remove_inline_comment(line: str) -> str:
        """
        Removes inline comments from a single line of code.

        :param line: A single line of Python code.
        :type line: str
        :return: The line without comments.
        :rtype: str
        """
        # Handle cases where '#' is inside a string
        in_single_quote = False
        in_double_quote = False
        escape = False
        for i, char in enumerate(line):
            if char == "\\" and not escape:
                escape = True
                continue
            if not escape:
                if char == "'" and not in_double_quote:
                    in_single_quote = not in_single_quote
                elif char == '"' and not in_single_quote:
                    in_double_quote = not in_double_quote
                elif char == "#" and not in_single_quote and not in_double_quote:
                    return line[:i].rstrip()
            escape = False
        return line.rstrip()

    cleaned_lines = []
    for line in source_code.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("#"):
            # Skip full-line comments
            continue
        else:
            # Remove inline comments
            cleaned_line = remove_inline_comment(line)
            cleaned_lines.append(cleaned_line)

    return "\n".join(cleaned_lines)


def append_file_contents(py_files):
    """
    Appends the contents of each .py file to the output file with a header and enhances readability.
    Preserves the first line of the file and removes all comments from the rest of the code.

    :param output_file: The path to the output file.
    :type output_file: Path
    :param py_files: List of paths to .py files.
    :type py_files: list[Path]
    """
    try:
        with setup_config.get_output_file_path().open("a", encoding="utf-8") as file:
            for py_file in py_files:
                separator = "########################################"
                # Write the first separator and header
                file.write(f"\n{separator}\n")
                # output_dir C:/Users/ME/Documents/Python/2026/Projects/test_program_file_structure
                # py_file is C:/Users/ME/Documents/Python/2026/Projects/test_program_file_structure/tests/test_text_utils.py
                # I want write 'test_program_file_structure/tests/test_text_utils.py'

                relative_py_file = py_file.relative_to(
                    setup_config.output_dir
                ).as_posix()
                last_directory = setup_config.output_dir.name
                file.write(
                    f"Here is my code for {last_directory}/{relative_py_file} BELOW:\n"
                )

                # file.write(f"Here is my code for {py_file.name} BELOW:\n")
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
                        file.write(cleaned_code)
                except UnicodeDecodeError:
                    file.write(
                        f"# Could not decode file {py_file} with UTF-8 encoding.\n\n"
                    )
                except IOError as e:
                    file.write(f"# Could not read file {py_file}: {e}\n\n")
                # End of Markdown code block
                file.write(f"```\n")
        logger.info(
            f"Python file contents appended to '{setup_config.get_output_file_path()}'."
        )
    except IOError as e:
        logger.info(
            f"An error occurred while appending to '{setup_config.get_output_file_path()}': {e}",
            file=sys.stderr,
        )


#######################################################################
# RAG Section
########################################################################
def rag_text():
    import shutil  # Ensure shutil is imported within the function or at the top of the script

    # Define the directory containing the text file and the persistent directory
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # persistent_directory = os.path.join(current_dir, "db", "rag_chroma_db")
    # os.makedirs(os.path.join(current_dir, "db"), exist_ok=True)
    # file_path = os.path.join(current_dir, "chat_gpt", "program_chat_gpt.txt")
    # chunks_dir = os.path.join(current_dir, "chat_gpt", "chunks")

    current_dir = setup_config.get_program_working_root_dir()
    persistent_directory = os.path.join(setup_config.get_db_dir(), "rag_chroma_db")
    file_path = setup_config.get_output_file_path()
    chunks_dir = setup_config.get_chunks_dir()

    if os.path.exists(chunks_dir):
        try:
            shutil.rmtree(chunks_dir)
            logger.info(f"Existing 'chunks' directory '{chunks_dir}' has been removed.")
        except Exception as e:
            logger.info(
                f"Error removing 'chunks' directory '{chunks_dir}': {e}",
                file=sys.stderr,
            )
            sys.exit(1)
    # Create the chunks directory if it doesn't exist
    try:
        os.makedirs(chunks_dir, exist_ok=True)
        logger.info(f"'chunks' directory '{chunks_dir}' has been created.")
    except Exception as e:
        logger.info(
            f"Error creating 'chunks' directory '{chunks_dir}': {e}", file=sys.stderr
        )
        sys.exit(1)

    # Check if the Chroma vector store already exists
    # if not os.path.exists(persistent_directory):
    logger.info("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    try:
        loader = TextLoader(file_path, encoding="utf-8", autodetect_encoding=True)
        documents = loader.load()
    except UnicodeDecodeError as e:
        # If autdetect failed, try again with latin-1 then raise
        try:
            loader = TextLoader(
                file_path, encoding="latin-1", autodetect_encoding=False
            )
            documents = loader.load()
        except Exception as e2:
            logger.info(f"Unicode decoding failed: {e} and fallback failed: {e2}")
            sys.exit(1)

    # Remove or replace any model special-token markers (like "<|endoftext|>") from text.
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

    logger.info("\n--- Using Token-based Splitting ---")
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
    logger.info("\n--- Document Chunks Information ---")
    logger.info(f"Number of document chunks: {len(docs)}")
    logger.info(f"Sample chunk:\n{docs[0].page_content}\n")

    # Write each chunk to a separate file
    for idx, doc in enumerate(docs, start=1):
        # chunk_number of
        chunk_number = f"# Chunk number: {idx} of {len(docs)}\n"
        chunk_filename = f"chunk{idx}.txt"
        chunk_path = os.path.join(chunks_dir, chunk_filename)
        try:
            with open(chunk_path, "w", encoding="utf-8") as chunk_file:
                chunk_file.write(chunk_number + "\n" + doc.page_content)
            logger.info(f"Written {chunk_filename}")
        except IOError as e:
            logger.info(f"Failed to write {chunk_filename}: {e}")

    logger.info("RAG DONE! Chunks have been written to the 'chunks' directory.")

    logger.info("RAG DONE!.")


def main() -> None:
    """
    Main function to execute the file structure generation process.
    """

    # Example usage of logger and LLM
    logger.info("Starting the file structure generation process.")

    try:
        start_dir = validate_path(setup_config.start_dir)
        setup_config.start_dir = start_dir
    except ValueError as e:
        logger.error(f"Invalid start path: {e}")
        sys.exit(1)
    logger.info(f"Scanning start path: {start_dir}")

    try:
        output_dir = validate_path(setup_config.output_dir)
        setup_config.output_dir = output_dir
    except ValueError as e:
        logger.error(f"Invalid output path: {e}")
        sys.exit(1)

    logger.info(f"Using output Directory: {setup_config.get_program_output_dir()}")

    # Add the program directory  to the exclusion setsS
    create_program_excluded()

    ###########################################################################
    # Starting to Generate the file structure
    ###########################################################################
    logger.info("\n--- Starting to Generate the file structure ---")
    logger.info("\n--- Scan Configuration ---")
    logger.info(f"Project Type: {setup_config.get_project_type()}")
    logger.info(f"Scanning start path: '{setup_config.start_dir}'")
    logger.info(f"Using output file: '{setup_config.get_output_file_path()}'")
    logger.info(
        f"Including 'tests' directory: {'Yes' if setup_config.include_tests_flag else 'No'}"
    )
    # Add custom header to the output file

    add_custom_header()
    structure_lines, py_files = generate_file_structure()
    write_directory_tree_to_file(structure_lines)
    append_file_contents(py_files)


if __name__ == "__main__":
    try:
        create_chat_gpt_directory_once(setup_config)
        main()
        rag_text()
        logger.info("Program DONE!.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
