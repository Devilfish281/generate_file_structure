# Today's Date: 
- 2026-08-07 19:26:21

Developer: Developer: 
# Project Title
- Generate File Structure



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



The File structure for my program is BELOW:
├── C:\Users\ME\Documents\Python\2026\Projects\generate_file_structure/
    ├── .env
    ├── .gitignore
    ├── README.md
    ├── ToRun.md
    ├── poetry.lock
    └── pyproject.toml
    ├── .vscode/
        ├── launch.json
        └── settings.json
    ├── custom_setting/
        ├── ai_coder_setting.md
        ├── ai_hello_setting.md
        ├── custom_setting.md
        ├── generate_file_structuree_setting.md
        ├── lmm_works_setting.md
        ├── power_bi_poc_setting.md
        ├── py_llm_pipeline_explorer_setting.md
        ├── sandcastle_setting.md
        ├── skills_my_prompts_setting.md
        ├── skills_prompt_setting.md
        ├── skills_setting.md
        ├── test_browser_mcp.md
        └── ts_llm_pipeline_explorer_setting.md
    ├── src/
        └── generate_file_structure/
            ├── __init__.py
            ├── generate_file.py
            ├── main.py
            ├── main_OLD.py
            ├── setup_config.py
            └── temp.py
            └── my_utils/
                ├── __init__.py
                ├── custom_settings_loader.py
                ├── directory_setup.py
                ├── env_loader.py
                ├── llm_loader.py
                ├── logger_setup.py
                ├── path_utils.py
                ├── token_usage.py
                └── token_usage_tier.json
    ├── tests/
        └── __init__.py
    └── var/
        └── logs/
            ├── reportlog.log
            ├── reportlog.log.1
            ├── reportlog.log.10
            ├── reportlog.log.2
            ├── reportlog.log.3
            ├── reportlog.log.4
            ├── reportlog.log.5
            ├── reportlog.log.6
            ├── reportlog.log.7
            ├── reportlog.log.8
            └── reportlog.log.9

########################################
Here is my code for generate_file_structure/README.md BELOW:
########################################

````markdown
## A description of the proram

`generate_file_structure.py` is a Python utility that creates an AI-friendly snapshot of a Python project. It scans a selected root directory, builds a formatted directory tree, writes the contents of discovered Python files into a single output report, optionally includes the `tests` directory and `pytest.ini`, then reloads that report with LangChain and splits it into token-based chunk files for later retrieval, search, or RAG-style AI processing.

---

## Description of what this program does

This program is a **project snapshot generator** for a Python codebase.

At a high level, it does **two big jobs**:

**Job 1: Build one large project report**

- It scans a project folder
- Builds a text-based directory tree
- Collects Python files
- Writes their contents into one big output text file
- Optionally includes the `tests` directory and `pytest.ini`

**Job 2: Split that big report into smaller chunks**

- It loads the generated text report using LangChain’s `TextLoader`
- It splits the report into token-based chunks using `TokenTextSplitter`
- It saves each chunk as its own `.txt` file for later AI/RAG use ([api.python.langchain.com][1])

So in simple words:

**This script turns a Python project into one AI-friendly text package, then breaks that package into smaller chunk files so an AI system can read or retrieve it more easily.**

---

## What file it creates

The main output file is:

`chat_gpt/program_chat_gpt.txt`

That file contains:

- a header
- the project directory tree
- the contents of discovered Python files
- optionally the contents of `pytest.ini`

Then the program creates chunk files in:

`chat_gpt/chunks/`

Examples:

- `chunk1.txt`
- `chunk2.txt`
- `chunk3.txt`

---

## Detailed step-by-step of what the program takes

## Step 1: Start the program

When the script runs, this block executes:

```python
if __name__ == "__main__":
    main()
    rag_text()
    print("Program DONE!.")
```

So it runs:

1. `main()`
2. `rag_text()`
3. prints `"Program DONE!."`

---

## Step 2: Figure out where the script is located

Inside `main()`, it gets:

- the full path to the current script
- the folder the script lives in

This is used so the program can:

- find `custom_header.txt`
- set default output paths
- avoid including itself in the final report

---

## Step 3: Read command-line arguments

The script accepts two optional arguments:

- `--root` or `-r`
  the folder to scan

- `--output` or `-o`
  the output text file path

If you do not provide them, it uses defaults:

- root = parent of the script directory
- output = `chat_gpt/program_chat_gpt.txt`

---

## Step 4: Ask whether to include the `tests` directory

The program asks:

`Do you want to include tests directory? (y/n):`

If you answer:

- `y` → it allows `tests`
- `n` → `tests` stays excluded

By default, `tests` is in `EXCLUDED_DIRS`, so this question controls whether that folder is brought back in.

---

## Step 5: Add the output folder name to excluded folders

The code does this:

```python
EXCLUDED_DIRS.add(args.output.parent.name)
```

That means the folder where the output file will be saved is excluded from scanning.

Why?

Because otherwise the script could accidentally include its own generated output inside the next run, which would make the report messy or recursive.

---

## Step 6: Create the output directory

`create_chat_gpt_directory(args.output)`

This makes sure the folder for the output file exists.

Example:

- if `chat_gpt/` does not exist, it creates it

---

## Step 7: Add a header to the output file

`add_custom_header(args.output, script_dir)`

That function calls `read_custom_header(script_dir)`.

Here is what happens:

### If `custom_header.txt` exists

- it reads that file
- uses that text as the header

### If `custom_header.txt` does not exist

- it uses the built-in default header string

Then it writes the header to the output file.

So the output file always starts with a project description section.

---

## Step 8: Ask whether to include all directories

Inside `generate_file_structure()`, the script asks:

`Do you want to include all directories? (y/n):`

If you answer:

- `y` → it includes every directory except excluded ones
- `n` → it asks you about each directory one by one

---

## Step 9: Walk through the project folder

The script uses:

```python
os.walk(root_dir)
```

This means it goes through the project folder recursively:

- folder by folder
- subfolder by subfolder
- file by file

For each directory, it removes excluded folder names from `dirs`.

The excluded set includes things like:

- `__pycache__`
- `.git`
- `venv`
- `.venv`
- `node_modules`
- `build`
- `db`
- `docs`
- `icons`
- `source`
- `tests` unless you said yes

---

## Step 10: Optionally ask about each folder

If you did **not** choose “include all directories,” the script asks about each directory:

`Do you want to include the directory 'X'? (y/n):`

If you answer `n`:

- that directory is removed from the walk
- its name is added to `EXCLUDED_DIRS`

So the scan becomes interactive.

---

## Step 11: Build the text directory tree

For each folder, the script calculates:

- its depth level
- indentation
- branch symbols like `├──` and `└──`

Then it adds lines such as:

- folder names
- file names

to the `lines` list.

That becomes the tree section of the report.

So this step creates the “shape” of the project.

---

## Step 12: Collect Python files

While scanning files, if a file ends with `.py`, the script adds it to `py_files`.

It also skips:

- the running script itself
- the output file itself

That prevents self-inclusion.

---

## Step 13: Write the directory tree to the output file

After the scan finishes, `main()` opens the output file in append mode and writes all tree lines.

So now the file contains:

1. the header
2. the directory structure

---

## Step 14: Append the contents of every Python file

If Python files were found, the script calls:

`append_file_contents(args.output, py_files)`

For each `.py` file, it writes:

- a separator line
- a label like
  `Here is my code for my_file.py BELOW:`
- a fenced Markdown code block
- the cleaned Python code

---

## Step 15: Remove comments from most of the Python code

Before writing each file’s code, the script does something special:

- it keeps the **first line** unchanged
- it removes comments from the **rest of the file**

This happens in `remove_comments_from_code()`.

That function:

- removes full-line comments
- removes inline comments
- tries not to break `#` characters inside strings

So the final report contains Python code with fewer comments, which may make the output shorter and more focused.

---

## Step 16: Optionally append `pytest.ini`

If you earlier said yes to tests, the script also looks for:

`pytest.ini`

If it exists, it appends it to the output file inside an `ini` code block.

So when tests are included, the report may contain:

- test folders
- Python test files
- `pytest.ini`

---

## Step 17: Start the chunking phase

After `main()` finishes, the script calls:

`rag_text()`

This is the second big phase.

Its job is to take the giant output report and split it into smaller files.

---

## Step 18: Prepare the chunk directory

Inside `rag_text()`:

- it defines the input file as
  `chat_gpt/program_chat_gpt.txt`
- it defines the chunks output folder as
  `chat_gpt/chunks`

If the chunks folder already exists:

- it deletes it completely

Then it recreates it fresh.

So each run starts with a clean chunk directory.

---

## Step 19: Verify the big report file exists

If `program_chat_gpt.txt` is missing, the program raises a `FileNotFoundError`.

That means chunking only works if the first phase succeeded.

---

## Step 20: Load the big text file with LangChain

The script uses LangChain’s `TextLoader` to load the report file into document objects. `TextLoader` is meant for reading text files into LangChain document format. ([api.python.langchain.com][1])

It first tries:

- UTF-8
- with `autodetect_encoding=True`

If that fails with a decoding error:

- it falls back to `latin-1`

That gives it a little protection against encoding problems.

---

## Step 21: Remove special token markers

The script removes these strings if they appear:

- `<|endoftext|>`
- `<|im_start|>`
- `<|im_end|>`

That is useful because some model/token markers can cause issues or add noise to RAG text.

---

## Step 22: Split the report into token-based chunks

The script uses `TokenTextSplitter` with:

- `chunk_size=32000`
- `chunk_overlap=100`
- `encoding_name="cl100k_base"`
- `disallowed_special=()`

`TokenTextSplitter` is a LangChain text splitter that splits content based on tokens rather than raw character count. ([api.python.langchain.com][2])

This means:

- each chunk is limited by token size
- nearby chunks overlap a little
- the overlap helps preserve context between chunks

---

## Step 23: Print chunk information

The program prints:

- the number of chunks
- a sample chunk

This is just for visibility while running the script.

---

## Step 24: Write each chunk to its own text file

For each chunk, it creates a file like:

- `chunk1.txt`
- `chunk2.txt`
- `chunk3.txt`

and writes the chunk’s text content into it.

Now the project snapshot has been transformed into smaller files that are easier to use for retrieval or AI processing.

---

## Step 25: Finish

At the end, it prints completion messages:

- `RAG DONE!`
- `Program DONE!.`

---

# Simple high-level summary

This program does the following:

1. Ask what parts of the project to include
2. Scan the project folder
3. Build a directory tree
4. Collect Python files
5. Write everything into one big text file
6. Optionally include `pytest.ini`
7. Load that big text file back in
8. Split it into token-sized chunks
9. Save each chunk as a separate file

---

# Very simple plain-English explanation

Think of this script like a **project packager for AI**.

It takes your Python project and creates:

- one big “project report” file
- many smaller “chunk” files

That makes it easier to:

- show your codebase to ChatGPT
- feed it into a RAG pipeline
- search pieces of the project later

---

# A few code issues and improvements

I also noticed some things that could be improved.

## 1. Unused imports

These imports appear unused:

- `io`
- `tokenize`
- `CharacterTextSplitter`

Also this variable is set but not used:

- `persistent_directory`

So those can probably be removed.

## 2. `comment_pattern` is never used

Inside `remove_comments_from_code()`:

```python
comment_pattern = re.compile(r"(?<!:)#.*")
```

That variable is created but never actually used.

So it should be removed unless you plan to use it later.

## 3. `is_last_item()` may not build a perfect tree

The tree drawing logic checks sibling directories only, not the full combined order of folders and files in the parent.

So the `├──` and `└──` formatting may sometimes be slightly off.

## 4. Global `EXCLUDED_DIRS` is being mutated

The script changes `EXCLUDED_DIRS` while running:

- removing `"tests"`
- adding excluded directory names
- adding the output folder name

That works, but it can make behavior harder to reason about.

A cleaner design would be:

- make a local copy of the excluded set inside `main()`
- pass it into functions

## 5. Comment removal is manual and can still be fragile

Your comment removal logic is thoughtful, but string parsing by hand can still fail in tricky cases such as:

- triple-quoted strings
- edge cases with quotes and escapes
- unusual Python syntax

If you want this to be more reliable, use Python’s tokenizer-based approach instead of manual scanning.

## 6. `rag_text()` depends on the exact output path

It always loads:

`chat_gpt/program_chat_gpt.txt`

So if the user passes a custom `--output`, `rag_text()` will still read the default file path, not the custom one.

That is a real design issue.

A better design would be:

- pass `args.output` into `rag_text()`

## 7. Deleting the whole chunks folder every run is aggressive

This is okay if intended, but it means previous chunk outputs are always destroyed.

That is fine for regeneration, but worth knowing.

---

# Practical action plan

Use this explanation for your project:

- **Purpose:** turn a Python project into one large text report plus smaller chunk files for AI use
- **Main phases:** scan project → write report → split report into chunks
- **Important outputs:** `program_chat_gpt.txt` and files inside `chat_gpt/chunks/`
- **Best improvements:** remove unused imports, pass output path into `rag_text()`, avoid mutating global `EXCLUDED_DIRS`, and improve tree/comment parsing logic

If you want, I can next turn this into:

1. a shorter school-style paragraph, or
2. a cleaner numbered workflow you can paste into your documentation.

[1]: https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.text.TextLoader.html?utm_source=chatgpt.com "TextLoader - API - LangChain"
[2]: https://api.python.langchain.com/en/latest/base/langchain_text_splitters.base.TokenTextSplitter.html?utm_source=chatgpt.com "TokenTextSplitter - API - LangChain"
````

########################################
Here is my code for generate_file_structure/ToRun.md BELOW:
########################################

````markdown
Use this command in PowerShell:

```powershell
python src\generate_file_structure\generate_file_structure.py --start-path "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure"
```

That works because your script is set up to read a command-line option named `--start-path` using Python’s `argparse` module, which is the standard library tool for command-line arguments. ([docs.python.org][1])

If you are already inside the project folder that contains `src`, this is the most direct command:

```powershell
python src\generate_file_structure\generate_file_structure.py --start-path "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure"
```

If you also want to set the output file yourself, use:

```powershell
python src\generate_file_structure\generate_file_structure.py --start-path "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure" --output "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure\chat_gpt\program_chat_gpt.txt"
```

The quotes around the Windows path are important because paths can contain spaces, and `argparse` expects the option value to be passed as one argument. ([Python documentation][1])

Step by step:

1. Open PowerShell.
2. `cd` into the folder where your project lives.
3. Run the command above.
4. When prompted, answer the include/exclude questions.

If your file still uses `--root` instead of `--start-path`, then run this version instead:

```powershell
python src\generate_file_structure\generate_file_structure.py --root "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure"
```

The script path itself may also be run with Python as a normal script, which matches the standard `if __name__ == "__main__":` script-entry pattern in Python. ([Python documentation][2])

Practical summary:
The command you most likely want is:

```powershell
python src\generate_file_structure\generate_file_structure.py --start-path "C:\Users\ME\Documents\Python\2026\Projects\test_program_file_structure"
```

If you want, I can give you the exact `cd` command too.

[1]: https://docs.python.org/3.10/search.html?q=argument&utm_source=chatgpt.com "Search — Python 3.10.20 documentation"
[2]: https://docs.python.org/3/faq/programming.html?utm_source=chatgpt.com "Programming FAQ"
````

########################################
Here is my code for generate_file_structure/pyproject.toml BELOW:
########################################

```toml
[project]
name = "generate-file-structure"
version = "0.1.0"
description = ""
authors = [
    {name = "Devilfish281",email = "Dobley@csu.fullerton.edu"}
]
readme = "README.md"
requires-python = ">=3.12,<3.14"
dependencies = [
    "python-dotenv (>=1.2.2,<2.0.0)",
    "langgraph (>=1.0.10,<2.0.0)",
    "langchain-core (>=1.2.17,<2.0.0)",
    "langchain (>=1.2.10,<2.0.0)",
    "langchain-community (>=0.4.1,<0.5.0)",
    "langchain-openai (>=1.1.10,<2.0.0)"
]

[tool.poetry]
packages = [{include = "generate_file_structure", from = "src"}]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

########################################
Here is my code for generate_file_structure/.vscode/launch.json BELOW:
########################################

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: generate_file_structure",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/generate_file_structure/generate_file_structure.py",
      "console": "integratedTerminal",
      "justMyCode": true,
      "args": [
        "--start-path",
        "C:\\Users\\ME\\Documents\\Python\\2026\\Projects\\test_program_file_structure",
        "--output",
        "C:\\Users\\ME\\Documents\\Python\\2026\\Projects\\test_program_file_structure\\chat_gpt\\program_chat_gpt.txt"
      ]
    },
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

########################################
Here is my code for generate_file_structure/.vscode/settings.json BELOW:
########################################

```json
{
  "python-envs.defaultEnvManager": "ms-python.python:poetry",
  "python-envs.defaultPackageManager": "ms-python.python:poetry"
}
```

########################################
Here is my code for generate_file_structure/custom_setting/ai_coder_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\ai_coder_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='ai_coder_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\Projects\ai_coder'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Projects\ai_coder'
```

########################################
Here is my code for generate_file_structure/custom_setting/ai_hello_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\ai_hello_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='ai_hello_file_structure.md'

INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\Projects\ai_hello'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Projects\ai_hello'
```

########################################
Here is my code for generate_file_structure/custom_setting/custom_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\custom_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='custom_generated_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=False
NEXT_JS_PROJECT_FLAG=True

START_DIR='C:\Users\ME\Documents\fullstack\Projects\asset_processing_web_app\nextjs'
OUTPUT_DIR=C:\Users\ME\Documents\fullstack\Projects\asset_processing_web_app
```

########################################
Here is my code for generate_file_structure/custom_setting/generate_file_structuree_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\generate_file_structuree_setting.md

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='generated_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\Projects\generate_file_structure'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Projects\generate_file_structure'
```

########################################
Here is my code for generate_file_structure/custom_setting/lmm_works_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\custom_setting\llm_works_main.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='llm_works_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=False
NEXT_JS_PROJECT_FLAG=True

START_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\source_code\how-llms-work\'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\source_code\how-llms-work\'
```

########################################
Here is my code for generate_file_structure/custom_setting/power_bi_poc_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\power_bi_poc_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='power_bi_poc_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\power_bi\Project\power_bi_poc'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\power_bi\Project\power_bi_poc'
```

########################################
Here is my code for generate_file_structure/custom_setting/py_llm_pipeline_explorer_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\py_llm_pipeline_explorer_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='py_llm_pipeline_explorer_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\projects\llm-pipeline-explorer\backend\'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\projects\llm-pipeline-explorer\backend\'
```

########################################
Here is my code for generate_file_structure/custom_setting/sandcastle_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\custom_setting/sandcastle_main.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='sandcastle_main_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=False
NEXT_JS_PROJECT_FLAG=True

START_DIR='C:\Users\ME\Documents\Python\2026\aihero\sandcastle-main'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\aihero'
```

########################################
Here is my code for generate_file_structure/custom_setting/skills_my_prompts_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\power_bi_poc_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='skills_file_structure.md'

# INCLUDE_TESTS_FLAG=False

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\skills\FLOW\'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\skills\'
```

########################################
Here is my code for generate_file_structure/custom_setting/skills_prompt_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\power_bi_poc_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='skills_file_structure.md'

# INCLUDE_TESTS_FLAG=False

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='C:\Users\ME\Documents\Python\2026\skills\wayfinder_chatgpt_prompt_pack\'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\skills\wayfinder_chatgpt_prompt_pack\'
```

########################################
Here is my code for generate_file_structure/custom_setting/skills_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\power_bi_poc_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='skills_file_structure.md'

# INCLUDE_TESTS_FLAG=False

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False


START_DIR='C:\Users\ME\Documents\Python\2026\source_code\skills_7_15_2026\skills'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\source_code\skills_7_15_2026\skills'
```

########################################
Here is my code for generate_file_structure/custom_setting/test_browser_mcp.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\test_browser_mcp.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='test_browser_mcp_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=True
NEXT_JS_PROJECT_FLAG=False

START_DIR='c:\Users\ME\Documents\Python\2026\Projects\test_browser_mcp'

OUTPUT_DIR='c:\Users\ME\Documents\Python\2026\Projects\test_browser_mcp'
```

########################################
Here is my code for generate_file_structure/custom_setting/ts_llm_pipeline_explorer_setting.md BELOW:
########################################

```markdown
# generate_file_structure\custom_setting\custom_setting\ts_llm_pipeline_explorer_setting.md

# Custom settings overrides

# Only the keys below should override `.env`.

OUTPUT_FILE_NAME='ts_llm_pipeline_explorer_file_structure.md'

# INCLUDE_TESTS_FLAG=True

# CUSTOM_HEADER_NAME='custom_header.md'

# CUSTOM_HEADER_BEGINNING_NAME='header_top.md'

# PYTHON_PROJECT_FLAG=True

# NEXT_JS_PROJECT_FLAG=False

# Project type flags

PYTHON_PROJECT_FLAG=False
NEXT_JS_PROJECT_FLAG=True

START_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\projects\llm-pipeline-explorer\frontend\'

OUTPUT_DIR='C:\Users\ME\Documents\Python\2026\Built_an_LLM_From_Scratch\projects\llm-pipeline-explorer\frontend\'
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/__init__.py BELOW:
########################################

```python
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/generate_file.py BELOW:
########################################

````python
# src/generate_file_structure/generate_file.py


import io
import os
import re
import sys
import tokenize
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter


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
):
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

    while True:
        include_all_response = (
            input("Do you want to include all directories? (y/n): ").strip().lower()
        )
        if include_all_response in {"y", "n"}:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"

    for root, dirs, files in os.walk(root_dir):
        root_path = Path(root)

        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        if not include_all:
            for d in dirs[:]:
                if d == "tests" and include_tests:
                    continue
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

        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            level = 0

        indent = "    " * level

        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "    "
        else:
            sub_indent = indent + "│   "

        files = sorted(files)
        for idx, f in enumerate(files):
            file_path = root_path / f
            if (
                file_path.resolve() == script_path.resolve()
                or file_path.resolve() == output_file.resolve()
            ):
                continue

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


def remove_comments_from_code(source_code: str) -> str:
    """
    Removes all comments from the provided Python source code without altering the original formatting.

    :param source_code: The original Python source code as a string.
    :type source_code: str
    :return: The source code without any comments.
    :rtype: str
    """

    comment_pattern = re.compile(r"(?<!:)#.*")

    def remove_inline_comment(line: str) -> str:
        """
        Removes inline comments from a single line of code.

        :param line: A single line of Python code.
        :type line: str
        :return: The line without comments.
        :rtype: str
        """
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
            continue
        else:
            cleaned_line = remove_inline_comment(line)
            cleaned_lines.append(cleaned_line)

    return "\n".join(cleaned_lines)


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
        with output_file.open("a", encoding="utf-8") as file:
            for py_file in py_files:
                separator = "########################################"
                file.write(f"\n{separator}\n")
                file.write(f"Here is my code for {py_file.name} BELOW:\n")
                file.write(f"{separator}\n\n")
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
                            cleaned_rest = remove_comments_from_code(rest_of_code)
                            if not first_line.endswith("\n"):
                                first_line += "\n"
                            cleaned_code = first_line + cleaned_rest

                        if cleaned_code and not cleaned_code.endswith(
                            "\n"
                        ):
                            cleaned_code += "\n"

                        file.write(cleaned_code)
                except UnicodeDecodeError:
                    file.write(
                        f"# Could not decode file {py_file} with UTF-8 encoding.\n\n"
                    )
                except IOError as e:
                    file.write(f"# Could not read file {py_file}: {e}\n\n")
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


def main() -> tuple[Path, Path]:
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
        default=None,
        help=(
            "Output file path (default: <start-path>/chat_gpt/program_chat_gpt.txt)\n"
            "Example: --output C:\\Users\\ME\\Documents\\Python\\2026\\Projects\\test_program_file_structure\\chat_gpt\\program_chat_gpt.txt"
        ),
    )

    args = parser.parse_args()

    try:
        start_path = validate_start_path(args.start_path)
    except ValueError as e:
        print(f"Invalid start path: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output is None:
        output_path = (
            start_path / "chat_gpt" / "program_chat_gpt.txt"
        ).resolve()
    else:
        output_path = args.output.expanduser().resolve()

    print(f"Scanning start path: '{start_path}'")
    print(f"Using output file: '{output_path}'")

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

    EXCLUDED_DIRS.add(output_path.parent.name)

    create_chat_gpt_directory(output_path)

    add_custom_header(output_path, script_dir)

    print("\n--- Starting to Generate the file structure ---")
    print("\n--- Scan Configuration ---")
    print(f"Scanning start path: '{start_path}'")
    print(f"Excluding script: '{script_path}'")
    print(f"Using output file: '{output_path}'")
    print(f"Including 'tests' directory: {'Yes' if include_tests else 'No'}")

    structure_lines, py_files = generate_file_structure(
        start_path,
        script_path,
        output_path,
        include_tests=include_tests,
    )

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

    if py_files:
        append_file_contents(output_path, py_files)
    else:
        print("No Python files found to append.")

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

    return output_path, start_path


def rag_text(output_file: Path, start_path: Path) -> None:
    import shutil

    script_dir = Path(__file__).resolve().parent

    output_file = output_file.expanduser().resolve()
    start_path = start_path.expanduser().resolve()

    chunks_dir = start_path / "chat_gpt" / "chunks"
    db_dir = start_path / "chat_gpt" / "db"
    db_dir.mkdir(parents=True, exist_ok=True)


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
    try:
        chunks_dir.mkdir(parents=True, exist_ok=True)
        print(f"'chunks' directory '{chunks_dir}' has been created.")
    except Exception as e:
        print(f"Error creating 'chunks' directory '{chunks_dir}': {e}", file=sys.stderr)
        sys.exit(1)

    print("Preparing generated report for token-based chunking...")

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
        try:
            loader = TextLoader(
                str(output_file), encoding="latin-1", autodetect_encoding=False
            )
            documents = loader.load()
        except Exception as e2:
            print(f"Unicode decoding failed: {e} and fallback failed: {e2}")
            sys.exit(1)

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

    print("\n--- Using Token-based Splitting ---")
    token_splitter = TokenTextSplitter(
        chunk_overlap=100,
        chunk_size=32000,
        encoding_name="cl100k_base",
        disallowed_special=(),
    )
    docs = token_splitter.split_documents(documents)


    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    if docs:
        print(f"Sample chunk:\n{docs[0].page_content}\n")
    else:
        print("No chunks were generated.\n")

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
    print("RAG DONE! DB directory is under 'chat_gpt/db'.")


if __name__ == "__main__":
    generated_output_file, start_path = main()
    rag_text(generated_output_file, start_path)
    print("Program DONE!.")
````

########################################
Here is my code for generate_file_structure/src/generate_file_structure/main.py BELOW:
########################################

````python
# src/generate_file_structure/main.py
import io
import os
import re
import sys
import tokenize
from datetime import datetime
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter

from generate_file_structure.my_utils.directory_setup import (
    create_chat_gpt_directory_once,
)
from generate_file_structure.my_utils.env_loader import load_dotenv_once
from generate_file_structure.my_utils.path_utils import validate_path
from generate_file_structure.setup_config import c_setup_config

load_dotenv_once()

setup_config = c_setup_config.get_instance()
logger = setup_config.get_logger()



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


INCLUDED_PYTHON_FILES = {
    ".py",
    ".toml",
    ".md",
    ".json",
    ".yaml",
    ".yml",
}


INCLUDED_PYTHON_TEST_FILES = {
    ".ini",
}
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
    "cache",
    ".next",
    "var",
    ".data",
}


INCLUDED_NEXTJS_FILES = {
    ".tsx",
    ".ts",
    ".css",
    ".json",
    ".md",
    ".mdx",
    ".yaml",
    ".yml",
    ".toml",
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

        if setup_config.get_project_type() == "python":
            if setup_config.include_tests_flag and "tests" in EXCLUDED_PYTHON_DIRS:
                EXCLUDED_PYTHON_DIRS.remove("tests")

        if setup_config.get_project_type() == "next_js":
            if setup_config.include_tests_flag and "tests" in EXCLUDED_NEXTJS_DIRS:
                EXCLUDED_NEXTJS_DIRS.remove("tests")

        main_dir = setup_config.get_program_output_dir()
        EXCLUDED_PYTHON_DIRS.add(main_dir.name)
        EXCLUDED_NEXTJS_DIRS.add(main_dir.name)

        if setup_config.get_project_type() == "python":
            logger.info(
                f"Excluded directories for Python project: {EXCLUDED_PYTHON_DIRS}"
            )

        if setup_config.get_project_type() == "next_js":
            logger.info(
                f"Excluded directories for Next.js project: {EXCLUDED_NEXTJS_DIRS}"
            )

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
    root_dir = setup_config.start_dir
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


    include_all_dir_flag = setup_config.include_all_dir_flag

    if include_all_dir_flag:
        include_all_response = "y"
        logger.info(
            "include_all_dir_flag=True; including all directories without prompting."
        )
    else:
        while True:
            include_all_response = (
                input("Do you want to include all directories? (y/n): ").strip().lower()
            )
            if include_all_response in {"y", "n"}:
                break
            else:
                logger.info("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"

    for root, dirs, files in os.walk(root_dir):
        root_path = Path(root)

        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        if not include_all:
            for child in dirs[:]:
                child_path = root_path / child
                if not child_path.is_dir():
                    continue

                if child == "tests" and setup_config.include_tests_flag:
                    continue

                while True:
                    response = (
                        input(
                            f"Do you want to include the directory '{child}'? (y/n): "
                        )
                        .strip()
                        .lower()
                    )
                    if response in {"y", "n"}:
                        break
                    logger.info("Invalid input. Please enter 'y' or 'n'.")

                if response == "y":
                    continue
                else:
                    dirs.remove(child)
                    excluded_dirs.add(child)
                    logger.info(f"Excluded directory: {child}")

        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            level = 0

        indent = "    " * level

        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "    "
        else:
            sub_indent = indent + "    "

        files = sorted(files)

        for idx, f in enumerate(files):
            file_path = root_path / f
            if file_path.resolve() == output_file.resolve():
                continue

            if file_path.suffix in included_file_suffixes:
                py_files_list.append(file_path)

            file_branch = "└── " if idx == len(files) - 1 else "├── "
            lines.append(f"{sub_indent}{file_branch}{f}\n")

    return lines, py_files_list


def write_directory_tree_to_file(structure_lines):

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


def remove_comments_from_code(source_code: str) -> str:
    """
    Removes real Python comments while preserving hash characters inside strings.

    This keeps Markdown headings such as '# Title' and '## Files' when they are
    inside triple-quoted strings.
    """

    if not source_code:
        return ""

    cleaned_lines = []
    in_triple_quoted_string = False
    triple_quote_delimiter = ""

    def find_next_triple_quote(line: str, start_index: int = 0) -> tuple[int, str]:
        single_quote_index = line.find("'''", start_index)
        double_quote_index = line.find('"""', start_index)

        if single_quote_index == -1 and double_quote_index == -1:
            return -1, ""

        if single_quote_index == -1:
            return double_quote_index, '"""'

        if double_quote_index == -1:
            return single_quote_index, "'''"

        if single_quote_index < double_quote_index:
            return single_quote_index, "'''"

        return double_quote_index, '"""'

    def remove_comment_outside_strings(line: str) -> str:
        in_single_quoted_string = False
        in_double_quoted_string = False
        escape_next_character = False
        index = 0

        while index < len(line):
            character = line[index]

            if character == "\\" and not escape_next_character:
                escape_next_character = True
                index += 1
                continue

            if not escape_next_character:
                if character == "'" and not in_double_quoted_string:
                    in_single_quoted_string = not in_single_quoted_string

                elif character == '"' and not in_single_quoted_string:
                    in_double_quoted_string = not in_double_quoted_string

                elif (
                    character == "#"
                    and not in_single_quoted_string
                    and not in_double_quoted_string
                ):
                    return line[:index].rstrip()

            escape_next_character = False
            index += 1

        return line.rstrip()

    for line in source_code.splitlines():
        working_index = 0
        should_keep_entire_line = in_triple_quoted_string

        while True:
            if in_triple_quoted_string:
                quote_index = line.find(triple_quote_delimiter, working_index)

                if quote_index == -1:
                    break

                in_triple_quoted_string = False
                working_index = quote_index + len(triple_quote_delimiter)
                should_keep_entire_line = True
                continue

            quote_index, quote_delimiter = find_next_triple_quote(
                line,
                working_index,
            )

            if quote_index == -1:
                break

            before_quote = line[:quote_index]

            if "#" in before_quote:
                break

            in_triple_quoted_string = True
            triple_quote_delimiter = quote_delimiter
            working_index = quote_index + len(quote_delimiter)
            should_keep_entire_line = True

        if should_keep_entire_line:
            cleaned_lines.append(line.rstrip())
            continue

        cleaned_line = remove_comment_outside_strings(line)

        if cleaned_line.strip():
            cleaned_lines.append(cleaned_line)
        elif line.strip() == "":
            cleaned_lines.append("")

    return "\n".join(cleaned_lines)


def prepare_file_content(source_path: Path, source_code: str) -> str:
    """
    Prepare one source file for inclusion in the generated report.

    Python files keep the existing behavior:
    - preserve the first line;
    - remove Python comments from the remaining source.

    Every non-Python file is returned exactly as read. This prevents Markdown,
    JSON, YAML, TOML, TypeScript, CSS, and other text files from being passed
    through the Python comment-removal logic.

    :param source_path: Path to the source file.
    :type source_path: Path
    :param source_code: Original source-file contents.
    :type source_code: str
    :return: Content to place in the generated report.
    :rtype: str
    """
    if source_path.suffix.lower() != ".py":
        return source_code

    if not source_code:
        return ""

    lines = source_code.splitlines()
    first_line = lines[0]
    rest_of_code = "\n".join(lines[1:])

    cleaned_rest = remove_comments_from_code(rest_of_code)

    if not first_line.endswith("\n"):
        first_line += "\n"

    return first_line + cleaned_rest


def get_markdown_language(source_path: Path) -> str:
    """
    Return the Markdown fenced-code language identifier for a source file.

    :param source_path: Path to the source file.
    :type source_path: Path
    :return: Markdown language identifier.
    :rtype: str
    """
    language_by_suffix = {
        ".py": "python",
        ".md": "markdown",
        ".mdx": "markdown",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".toml": "toml",
        ".ini": "ini",
        ".ts": "typescript",
        ".tsx": "tsx",
        ".css": "css",
    }

    return language_by_suffix.get(
        source_path.suffix.lower(),
        "text",
    )


def get_safe_markdown_fence(source_code: str) -> str:
    """
    Return an outer Markdown code fence that cannot be closed accidentally
    by a backtick fence contained inside the source file.

    :param source_code: Source-file contents.
    :type source_code: str
    :return: Safe Markdown fence.
    :rtype: str
    """
    backtick_runs = re.findall(r"`+", source_code)

    longest_backtick_run = max(
        (len(run) for run in backtick_runs),
        default=0,
    )

    return "`" * max(3, longest_backtick_run + 1)


def append_file_contents(py_files):
    """
    Append included source files to the generated report.

    Python files have Python comments removed using the existing Python-only
    cleaning behavior.

    Every non-Python source file is copied exactly as read. This preserves
    Markdown headings, JSON values containing '#', YAML comments, TOML
    comments, and all other non-Python source text.

    Each source file is wrapped in a dynamically sized Markdown fence so
    embedded Markdown code fences cannot accidentally terminate the outer
    generated-report block.

    :param py_files: List of source-file paths to append.
    :type py_files: list[Path]
    """
    try:
        with setup_config.get_output_file_path().open(
            "a",
            encoding="utf-8",
        ) as file:
            for py_file in py_files:
                separator = "########################################"

                file.write(f"\n{separator}\n")

                relative_py_file = py_file.relative_to(
                    setup_config.output_dir
                ).as_posix()

                last_directory = setup_config.output_dir.name

                file.write(
                    f"Here is my code for "
                    f"{last_directory}/{relative_py_file} BELOW:\n"
                )

                logger.info(
                    f"Here is my code for "
                    f"{last_directory}/{relative_py_file} BELOW:\n"
                )

                file.write(f"{separator}\n\n")

                try:
                    with py_file.open("r", encoding="utf-8") as py_f:
                        source_code = py_f.read()

                    prepared_code = prepare_file_content(
                        py_file,
                        source_code,
                    )

                    markdown_language = get_markdown_language(py_file)

                    markdown_fence = get_safe_markdown_fence(prepared_code)

                    file.write(f"{markdown_fence}{markdown_language}\n")

                    file.write(prepared_code)

                    if prepared_code and not prepared_code.endswith("\n"):
                        file.write("\n")

                    file.write(f"{markdown_fence}\n")

                except UnicodeDecodeError:
                    file.write(
                        "```text\n"
                        f"# Could not decode file {py_file} "
                        "with UTF-8 encoding.\n"
                        "```\n"
                    )

                except IOError as e:
                    file.write(
                        "```text\n" f"# Could not read file {py_file}: {e}\n" "```\n"
                    )

        logger.info(
            f"Source file contents appended to "
            f"'{setup_config.get_output_file_path()}'."
        )

    except IOError as e:
        logger.error(
            f"An error occurred while appending to "
            f"'{setup_config.get_output_file_path()}': {e}"
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
        create_chat_gpt_directory_once(setup_config, logger)
        main()
        rag_text()
        logger.info("Program DONE!.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
````

########################################
Here is my code for generate_file_structure/src/generate_file_structure/main_OLD.py BELOW:
########################################

````python
# src/generate_file_structure/main.py
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter

from generate_file_structure.my_utils.directory_setup import (
    create_chat_gpt_directory_once,
)
from generate_file_structure.my_utils.env_loader import load_dotenv_once
from generate_file_structure.my_utils.path_utils import validate_path
from generate_file_structure.setup_config import c_setup_config

load_dotenv_once()
setup_config = c_setup_config.get_instance()
logger = setup_config.get_logger()


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
INCLUDED_PYTHON_FILES = {
    ".py",
    ".toml",
}
INCLUDED_PYTHON_TEST_FILES = {
    ".ini",
}
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
    "cache",
    ".next",
    "var",
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

        if setup_config.get_project_type() == "python":
            if not setup_config.include_tests_flag and "tests" in EXCLUDED_PYTHON_DIRS:
                EXCLUDED_PYTHON_DIRS.remove("tests")

        if setup_config.get_project_type() == "next_js":
            if not setup_config.include_tests_flag and "tests" in EXCLUDED_NEXTJS_DIRS:
                EXCLUDED_NEXTJS_DIRS.remove("tests")

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

    while True:
        include_all_response = (
            input("Do you want to include all directories? (y/n): ").strip().lower()
        )
        if include_all_response in {"y", "n"}:
            break
        else:
            logger.info("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"
    for root, dirs, files in os.walk(root_dir):
        root_path = Path(root)

        dirs[:] = [d for d in dirs if d not in excluded_dirs]

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

        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            level = 0

        indent = "    " * level

        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "    "
        else:
            sub_indent = indent + "    "

        files = sorted(files)

        for idx, f in enumerate(files):
            file_path = root_path / f
            if file_path.resolve() == output_file.resolve():
                continue

            if file_path.suffix in included_file_suffixes:
                py_files_list.append(file_path)

            file_branch = "└── " if idx == len(files) - 1 else "├── "
            lines.append(f"{sub_indent}{file_branch}{f}\n")

    return lines, py_files_list


def write_directory_tree_to_file(structure_lines):

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


def remove_comments_from_code(source_code: str) -> str:
    """
    Removes all comments from the provided Python source code without altering the original formatting.

    :param source_code: The original Python source code as a string.
    :type source_code: str
    :return: The source code without any comments.
    :rtype: str
    """

    comment_pattern = re.compile(r"(?<!:)#.*")

    def remove_inline_comment(line: str) -> str:
        """
        Removes inline comments from a single line of code.

        :param line: A single line of Python code.
        :type line: str
        :return: The line without comments.
        :rtype: str
        """
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
            continue
        else:
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
                file.write(f"\n{separator}\n")

                relative_py_file = py_file.relative_to(
                    setup_config.output_dir
                ).as_posix()
                last_directory = setup_config.output_dir.name
                file.write(
                    f"Here is my code for {last_directory}/{relative_py_file} BELOW:\n"
                )

                file.write(f"{separator}\n\n")
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
                            cleaned_rest = remove_comments_from_code(rest_of_code)
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
                file.write(f"```\n")
        logger.info(
            f"Python file contents appended to '{setup_config.get_output_file_path()}'."
        )
    except IOError as e:
        logger.info(
            f"An error occurred while appending to '{setup_config.get_output_file_path()}': {e}",
            file=sys.stderr,
        )


def rag_text():
    import shutil


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
    try:
        os.makedirs(chunks_dir, exist_ok=True)
        logger.info(f"'chunks' directory '{chunks_dir}' has been created.")
    except Exception as e:
        logger.info(
            f"Error creating 'chunks' directory '{chunks_dir}': {e}", file=sys.stderr
        )
        sys.exit(1)

    logger.info("Persistent directory does not exist. Initializing vector store...")

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    try:
        loader = TextLoader(file_path, encoding="utf-8", autodetect_encoding=True)
        documents = loader.load()
    except UnicodeDecodeError as e:
        try:
            loader = TextLoader(
                file_path, encoding="latin-1", autodetect_encoding=False
            )
            documents = loader.load()
        except Exception as e2:
            logger.info(f"Unicode decoding failed: {e} and fallback failed: {e2}")
            sys.exit(1)

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

    logger.info("\n--- Using Token-based Splitting ---")
    token_splitter = TokenTextSplitter(
        chunk_overlap=100,
        chunk_size=32000,
        encoding_name="cl100k_base",
        disallowed_special=(),
    )
    docs = token_splitter.split_documents(documents)


    logger.info("\n--- Document Chunks Information ---")
    logger.info(f"Number of document chunks: {len(docs)}")
    logger.info(f"Sample chunk:\n{docs[0].page_content}\n")

    for idx, doc in enumerate(docs, start=1):
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

    create_program_excluded()

    logger.info("\n--- Starting to Generate the file structure ---")
    logger.info("\n--- Scan Configuration ---")
    logger.info(f"Project Type: {setup_config.get_project_type()}")
    logger.info(f"Scanning start path: '{setup_config.start_dir}'")
    logger.info(f"Using output file: '{setup_config.get_output_file_path()}'")
    logger.info(
        f"Including 'tests' directory: {'Yes' if setup_config.include_tests_flag else 'No'}"
    )

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
````

########################################
Here is my code for generate_file_structure/src/generate_file_structure/setup_config.py BELOW:
########################################

```python
# src/generate_file_structure/setup_config.py


import logging
import os
import threading
from asyncio.log import logger
from pathlib import Path

from typing import ClassVar, Optional

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, ConfigDict, Field

from generate_file_structure.my_utils.custom_settings_loader import (
    load_custom_settings_once,
)
from generate_file_structure.my_utils.env_loader import load_dotenv_once
from generate_file_structure.my_utils.llm_loader import get_llm_or_init
from generate_file_structure.my_utils.logger_setup import setup_logger

try:
    load_dotenv_once()
except Exception:
    pass




LOGGER_PROJECT_NAME = "generate_file_structure"


class c_setup_config(BaseModel):
    """
    Singleton-style setup/config model for runtime configuration and shared objects.

    :ivar log_prompt_flag: Whether prompt logging is enabled.
    :vartype log_prompt_flag: bool
    :ivar llm: Cached LangChain OpenAI chat model instance.
    :vartype llm: Optional[ChatOpenAI]
    :ivar logger: Cached logger instance.
    :vartype logger: Optional[logging.Logger]
    :ivar max_chunk_size_bytes: Maximum chunk size for processing.
    :vartype max_chunk_size_bytes: int
    :ivar openai_model: Default OpenAI model name.
    :vartype openai_model: str
    :ivar testing_flag: Primary testing mode flag.
    :vartype testing_flag: bool
    :ivar testing_flag2: Secondary testing mode flag.
    :vartype testing_flag2: bool
    """



    start_dir: Path = Field(
        default_factory=lambda: Path(
            c_setup_config.get_setting_value("START_DIR", ".").strip().strip("'\"")
        ),
        description="Path to the directory to generate file structure for.",
    )

    output_dir: Path = Field(
        default_factory=lambda: Path(
            c_setup_config.get_setting_value("OUTPUT_DIR", "./").strip().strip("'\"")
        ),
        description="Path to the output file for the generated file structure.",
    )

    output_file_name: str = Field(
        default_factory=lambda: c_setup_config.get_setting_value(
            "OUTPUT_FILE_NAME", "generated_file_structure.md"
        )
        .strip()
        .strip("'\""),
        description="Name of the output file for the generated file structure.",
    )


    python_project_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool(
            "PYTHON_PROJECT_FLAG", True
        ),
        description="Flag to indicate if the application is running as a Python project.",
    )

    next_js_project_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool(
            "NEXT_JS_PROJECT_FLAG", False
        ),
        description="Flag to indicate if the application is running as a Next.js project.",
    )


    custom_header_name: str = Field(
        default_factory=lambda: c_setup_config.get_setting_value(
            "CUSTOM_HEADER_NAME", "custom_header.md"
        )
        .strip()
        .strip("'\""),
        description="Name of the custom header file to include at the top of the output file.",
    )

    custom_header_beginning_name: str = Field(
        default_factory=lambda: c_setup_config.get_setting_value(
            "CUSTOM_HEADER_BEGINNING_NAME", "beginning.md"
        )
        .strip()
        .strip("'\""),
        description="Name of the custom header file to include at the top of the output file.",
    )

    include_tests_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool(
            "INCLUDE_TESTS_FLAG", False
        ),
        description="Flag to indicate if the application should include test directories.",
    )

    include_all_dir_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool(
            "AUTO_INCLUDE_ALL_DIR_FLAG", False
        ),
        description="Flag to indicate if the application should include all directories.",
    )


    max_chunk_size_bytes: int = Field(
        default_factory=lambda: int(
            c_setup_config.get_setting_value(
                "MAX_CHUNK_SIZE_BYTES", str(24 * 1024 * 1024)
            )
        ),
        description="Maximum chunk size in bytes for processing large files.",
    )

    openai_model: str = Field(
        default_factory=lambda: c_setup_config.get_setting_value(
            "OPENAI_MODEL", "gpt-5.1"
        )
        .strip()
        .strip("'\""),
        description="Default OpenAI model to use for LLM interactions.",
    )

    testing_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool("TESTING_FLAG", False),
        description="Flag to indicate if the application is running in testing mode.",
    )

    testing_flag2: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool("TESTING_FLAG2", False),
        description="Flag to indicate if the application is running in testing mode level 2.",
    )

    log_prompt_flag: bool = Field(
        default_factory=lambda: c_setup_config.get_setting_bool(
            "LOG_PROMPT_FLAG", False
        ),
        description="Enable logging of prompts.",
    )

    llm: Optional[ChatOpenAI] = Field(default=None, description="LLM Configuration.")

    logger: Optional[logging.Logger] = Field(
        default=None, description="Logger Configuration."
    )

    _instance: ClassVar[Optional["c_setup_config"]] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def get_custom_settings_path(cls) -> Path:
        project_root = Path(__file__).resolve().parents[2]
        custom_settings_file_name = (
            os.getenv("CUSTOM_SETTING_FILE_NAME", "custom_setting.md")
            .strip()
            .strip("'\"")
        )
        return project_root / "custom_setting" / custom_settings_file_name

    @classmethod
    def get_custom_settings(cls) -> dict[str, str]:
        return load_custom_settings_once(cls.get_custom_settings_path())

    @classmethod
    def get_setting_value(cls, key: str, default: str = "") -> str:
        custom_settings = cls.get_custom_settings()
        if key in custom_settings:
            return custom_settings[key]
        return os.getenv(key, default)

    @classmethod
    def get_setting_bool(cls, key: str, default: bool = False) -> bool:
        raw_value = cls.get_setting_value(key, str(default))
        return raw_value.strip().lower() in {"1", "true", "yes", "y", "on"}

    @staticmethod
    def get_required_env(key: str) -> str:
        """
        Return a required environment variable after trimming whitespace and quotes.

        :param key: Environment variable name.
        :type key: str
        :return: Cleaned environment variable value.
        :rtype: str
        :raises ValueError: If the environment variable is missing or empty.
        """
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable: {key}")
        return value.strip().strip("'\"")

    @staticmethod
    def env_bool(name: str, default: bool = False) -> bool:
        """
        Convert an environment variable to a boolean.

        :param name: Environment variable name.
        :type name: str
        :param default: Value to use if the variable is not set.
        :type default: bool
        :return: Parsed boolean value.
        :rtype: bool
        """
        raw = os.getenv(name)
        if raw is None:
            return default
        return raw.strip().lower() in {"1", "true", "yes", "y", "on"}

    @staticmethod
    def _mask_key(value: Optional[str]) -> Optional[str]:
        """
        Mask a sensitive string for safe display.

        :param value: Secret value to mask.
        :type value: Optional[str]
        :return: Masked value.
        :rtype: Optional[str]
        """
        if not value:
            return None
        s = str(value)
        return f"{s[:4]}...{s[-4:]}" if len(s) > 8 else "***"

    def set_logger(self, logger: logging.Logger) -> None:
        self.logger = logger

    def get_logger(self) -> logging.Logger:
        if self.logger is None:

            self.logger = setup_logger(LOGGER_PROJECT_NAME)
            self.logger.info("logger Started!")
        return self.logger

    def get_llm(self) -> ChatOpenAI:
        """Return initialized LLM, initializing it once if needed."""

        return get_llm_or_init(
            self,
            temperature=0.0,
            streaming=True,
        )

    def get_program_working_root_dir(self) -> Path:
        return self.output_dir

    def get_program_output_dir(self) -> Path:
        return self.output_dir / "chat_gpt"

    def get_chunks_dir(self) -> Path:
        return self.get_program_output_dir() / "chunks"

    def get_db_dir(self) -> Path:
        return self.get_program_output_dir() / "db"

    def get_output_file_path(self) -> Path:
        return self.get_program_output_dir() / self.output_file_name

    def get_custom_header_dir(self) -> Path:
        custom_header_path = self.get_program_output_dir() / "header"
        return custom_header_path

    def get_custom_header_location(self) -> Path:
        custom_header_location = self.get_custom_header_dir() / self.custom_header_name
        return custom_header_location

    def get_custom_header_beginning_location(self) -> Path:
        custom_header_location = (
            self.get_custom_header_dir() / self.custom_header_beginning_name
        )
        return custom_header_location


    def get_project_type(self) -> str:
        if self.python_project_flag:
            return "python"
        elif self.next_js_project_flag:
            return "next_js"
        else:
            return "python"

    """
    setup_config = c_setup_config.get_instance()
    print(setup_config)
    ##########################################
    setup_config = c_setup_config.get_instance()
    config_repr = repr(setup_config)
    print(config_repr)
    """

    def __repr__(self) -> str:
        """
        Return a readable string representation of the config object.

        :return: Readable configuration summary.
        :rtype: str
        """
        return (
            "c_setup_config("
            f"testing_flag={self.testing_flag!r}, "
            f"testing_flag2={self.testing_flag2!r}, "
            f"log_prompt_flag={self.log_prompt_flag!r}, "
            f"max_chunk_size_bytes={self.max_chunk_size_bytes!r}, "
            f"openai_model={self.openai_model!r}, "
            f"llm={'Initialized' if self.llm else 'Not Initialized'}, "
            f"logger={'Initialized' if self.logger else 'Not Initialized'}"
            ")"
        )

    """
    import json

    config_json = json.dumps(setup_config.to_dict(), indent=4)
    print(config_json)
    #################################
    setup_config = c_setup_config.get_instance()
    config_dict = setup_config.to_dict()
    print(config_dict)

    """

    def to_dict(self) -> dict:
        """
        Convert the configuration object to a plain dictionary.

        :return: Dictionary view of current config and runtime state.
        :rtype: dict
        """
        return {
            "testing_flag": self.testing_flag,
            "testing_flag2": self.testing_flag2,
            "log_prompt_flag": self.log_prompt_flag,
            "max_chunk_size_bytes": self.max_chunk_size_bytes,
            "openai_model": self.openai_model,
            "llm_initialized": self.llm is not None,
            "logger_initialized": self.logger is not None,
        }

    def validate_initialization(self) -> None:
        """
        Validate that required runtime objects and environment values are initialized.

        :raises ValueError: If required dependencies are missing.
        """
        if self.logger is None:
            raise ValueError("logger must be initialized.")

        if self.llm is None:
            raise ValueError("llm must be initialized.")

        apikey = os.getenv("OPENAI_API_KEY", "").strip()
        if not apikey:
            self.logger.error("OPENAI_API_KEY environment variable not set")
            raise ValueError("OPENAI_API_KEY environment variable not set")

        if len(apikey) < 20:
            self.logger.error("OPENAI_API_KEY looks too short to be valid")
            raise ValueError("OPENAI_API_KEY looks too short to be valid")

    """
        Pydantic normally expects fields to be “pydantic-friendly” types (str/int/dict/BaseModel/etc). You have fields like:

        llm: Optional[ChatOpenAI]

        logger: Optional[logging.Logger]

        tavily_client: Optional[TavilyClient]

        Those are “arbitrary” Python objects. Setting arbitrary_types_allowed=True tells Pydantic:
        “Don't try to validate/parse these types—just allow them as-is.”
        This is the standard Pydantic v2 way to configure a model via model_config
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/temp.py BELOW:
########################################

```python
def generate_file_structure():
    """
    Generates the directory structure of the given root directory and collects .py files.

    :return: Tuple containing list of directory structure lines and list of .py file paths.
    :rtype: tuple[list[str], list[Path]]
    """
    lines = ["The File structure for my program is BELOW:\n"]
    py_files_list = []
    root_dir = setup_config.start_dir
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

    while True:
        include_all_response = (
            input("Do you want to include all directories? (y/n): ").strip().lower()
        )
        if include_all_response in {"y", "n"}:
            break
        else:
            logger.info("Invalid input. Please enter 'y' or 'n'.")

    include_all = include_all_response == "y"
    for root, dirs, files in os.walk(root_dir):
        root_path = Path(root)

        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        if not include_all:
            for child in dirs[:]:
                child_path = root_path / child
                if not child_path.is_dir():
                    continue

                if child == "tests" and setup_config.include_tests_flag:
                    continue

                while True:
                    response = (
                        input(
                            f"Do you want to include the directory '{child}'? (y/n): "
                        )
                        .strip()
                        .lower()
                    )
                    if response in {"y", "n"}:
                        break
                    logger.info("Invalid input. Please enter 'y' or 'n'.")

                if response == "y":
                    continue
                else:
                    dirs.remove(child)
                    excluded_dirs.add(child)
                    logger.info(f"Excluded directory: {child}")

        try:
            relative_path = root_path.relative_to(root_dir)
            level = len(relative_path.parts)
        except ValueError:
            level = 0

        indent = "    " * level

        dir_name = root_path.name if root_path != root_dir else str(root_path.resolve())

        branch = "└── " if is_last_item(root_path, dirs, files) else "├── "
        lines.append(f"{indent}{branch}{dir_name}/\n")

        if is_last_item(root_path, dirs, files):
            sub_indent = indent + "    "
        else:
            sub_indent = indent + "    "

        files = sorted(files)

        for idx, f in enumerate(files):
            file_path = root_path / f
            if file_path.resolve() == output_file.resolve():
                continue

            if file_path.suffix in included_file_suffixes:
                py_files_list.append(file_path)

            file_branch = "└── " if idx == len(files) - 1 else "├── "
            lines.append(f"{sub_indent}{file_branch}{f}\n")

    return lines, py_files_list
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/__init__.py BELOW:
########################################

```python
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/custom_settings_loader.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/custom_settings_loader.py
import threading
from pathlib import Path

_CUSTOM_SETTINGS_CACHE = None
_CUSTOM_SETTINGS_LOCK = threading.Lock()


def _clean_value(raw_value: str) -> str:
    """Normalize a parsed value from `custom_setting.md`."""
    value = raw_value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def load_custom_settings_once(
    custom_settings_path: Path,
) -> dict[str, str]:
    """
    Read `custom_setting.md` exactly once per process and return parsed key/value overrides.
    Ignore blank lines and lines that begin with `#`.
    """
    global _CUSTOM_SETTINGS_CACHE

    if _CUSTOM_SETTINGS_CACHE is not None:
        return dict(_CUSTOM_SETTINGS_CACHE)

    with _CUSTOM_SETTINGS_LOCK:
        if _CUSTOM_SETTINGS_CACHE is not None:
            return dict(_CUSTOM_SETTINGS_CACHE)

        custom_settings_path = Path(custom_settings_path).expanduser().resolve()
        parsed_settings: dict[str, str] = {}

        if custom_settings_path.exists():
            content = custom_settings_path.read_text(encoding="utf-8")
            for line in content.splitlines():
                stripped_line = line.strip()

                if not stripped_line:
                    continue

                if stripped_line.startswith("#"):
                    continue

                if "=" not in stripped_line:
                    continue

                key, raw_value = stripped_line.split("=", 1)
                key = key.strip()
                raw_value = raw_value.strip()

                if not key:
                    continue

                parsed_settings[key] = _clean_value(raw_value)

        _CUSTOM_SETTINGS_CACHE = parsed_settings
        return dict(_CUSTOM_SETTINGS_CACHE)
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/directory_setup.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/directory_setup.py
import threading
from pathlib import Path

_DIRECTORY_INITIALIZED = False
_DIRECTORY_LOCK = threading.Lock()


def create_chat_gpt_directory_once(setup_config, logger) -> bool:
    """
    Create the `chat_gpt` working directories exactly once per process.

    The function creates the main output directory plus the `chunks`, `db`,
    and `header` subdirectories in a thread-safe way.

    :param setup_config: Shared setup/config object that provides directory paths.
    :type setup_config: object
    :return: True if this call performed the directory creation step, otherwise False.
    :rtype: bool
    :raises ValueError: If a required directory path is missing or if directory creation fails.
    """
    global _DIRECTORY_INITIALIZED

    if _DIRECTORY_INITIALIZED:
        return False

    with _DIRECTORY_LOCK:
        if _DIRECTORY_INITIALIZED:
            return False

        main_dir = getattr(setup_config, "get_program_output_dir", None)
        logger.debug(f"Retrieved main_dir from setup_config: {main_dir}")

        chunks_dir = getattr(setup_config, "get_chunks_dir", None)
        logger.debug(f"Retrieved chunks_dir from setup_config: {chunks_dir}")

        db_dir = getattr(setup_config, "get_db_dir", None)
        header_dir = getattr(setup_config, "get_custom_header_dir", None)

        if main_dir is None or not callable(main_dir):
            raise ValueError(
                "setup_config.get_program_output_dir is missing or not callable."
            )
        if chunks_dir is None or not callable(chunks_dir):
            raise ValueError("setup_config.get_chunks_dir is missing or not callable.")
        if db_dir is None or not callable(db_dir):
            raise ValueError("setup_config.get_db_dir is missing or not callable.")
        if header_dir is None or not callable(header_dir):
            raise ValueError(
                "setup_config.get_custom_header_dir is missing or not callable."
            )

        resolved_main_dir = Path(main_dir()).expanduser().resolve()
        resolved_chunks_dir = Path(chunks_dir()).expanduser().resolve()
        resolved_db_dir = Path(db_dir()).expanduser().resolve()
        resolved_header_dir = Path(header_dir()).expanduser().resolve()

        try:
            resolved_main_dir.mkdir(parents=True, exist_ok=True)
            resolved_chunks_dir.mkdir(parents=True, exist_ok=True)
            resolved_db_dir.mkdir(parents=True, exist_ok=True)
            resolved_header_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise ValueError(f"Failed to create chat_gpt directories: {e}") from e

        _DIRECTORY_INITIALIZED = True
        return True
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/env_loader.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/env_loader.py
import threading

from dotenv import load_dotenv

_ENV_LOADED = False
_ENV_LOCK = threading.Lock()


def load_dotenv_once(*, override: bool = False) -> bool:
    """Load .env exactly once per process. Returns True if this call performed loading."""
    global _ENV_LOADED
    if _ENV_LOADED:
        return False
    with _ENV_LOCK:
        if _ENV_LOADED:
            return False
        load_dotenv(override=override)
        _ENV_LOADED = True
        return True
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/llm_loader.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/llm_loader.py
import threading
from typing import Optional

from langchain_openai import ChatOpenAI

_LLM_INITIALIZED = False
_LLM_LOCK = threading.Lock()


def init_llm_once(
    setup_config,
    *,
    temperature: float = 0.0,
    streaming: bool = True,
) -> bool:
    """
    Initialize setup_config.llm exactly once per process.

    Returns True if THIS call performed initialization, otherwise False.
    """
    global _LLM_INITIALIZED

    if _LLM_INITIALIZED and setup_config.llm is not None:
        return False

    with _LLM_LOCK:
        if _LLM_INITIALIZED and setup_config.llm is not None:
            return False

        model = getattr(setup_config, "openai_model", None)
        if not model:
            raise ValueError(
                "setup_config.openai_model is missing/empty; cannot init LLM."
            )

        setup_config.llm = ChatOpenAI(
            temperature=temperature,
            model=model,
            streaming=streaming,
        )

        _LLM_INITIALIZED = True
        return True


def get_llm_or_init(
    setup_config,
    *,
    temperature: float = 0.0,
    streaming: bool = True,
) -> ChatOpenAI:
    """
    Return setup_config.llm, initializing it once if needed.
    """
    if setup_config.llm is None or not _LLM_INITIALIZED:
        init_llm_once(setup_config, temperature=temperature, streaming=streaming)
    if setup_config.llm is None:
        raise ValueError("LLM initialization failed; setup_config.llm is still None.")
    return setup_config.llm
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/logger_setup.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/logger_setup.py

import json
import logging
import os
import queue
import sys
import threading
from contextlib import contextmanager
from logging.handlers import RotatingFileHandler
from pathlib import Path

from generate_file_structure.my_utils.env_loader import load_dotenv_once


try:
    load_dotenv_once()
except Exception:
    pass




if os.name == "nt":
    os.system("chcp 65001 >nul 2>&1")


def get_default_config():
    """
    Get the default logging configuration.

    :return: A dictionary containing the default logging configuration.
    :rtype: dict

    **Default Configuration Keys:**
        - `log_level` (str): Logging level, default is "INFO".
        - `log_dir` (str): Directory for log files, default is the current working directory.
        - `log_max_bytes` (int): Max size of log files in bytes, default is 5 MB.
        - `log_backup_count` (int): Number of backup log files, default is 5.
        - `enable_console` (bool): Enable console logging, default is True.
        - `enable_file` (bool): Enable file logging, default is True.
    """
    config = {
        "log_level": "INFO",
        "log_dir_pwd": os.getcwd(),
        "log_dir_extened": "",
        "log_dir_path": os.getcwd(),
        "log_max_bytes": 5
        * 1024
        * 1024,
        "log_backup_count": 5,
        "enable_console": True,
        "enable_file": True,
    }
    return config


def load_config(config_file=None):
    """
    Load logging configuration from a JSON file or environment variables, with overrides.

    :param config_file: Path to the JSON configuration file. If None, defaults will be used.
    :type config_file: str, optional

    :return: A dictionary containing the logging configuration.
    :rtype: dict

    **Default Configuration Keys:**
        - `log_level` (str): Logging level, default is "INFO".
        - `log_dir` (str): Directory for log files, default is the current working directory.
        - `log_max_bytes` (int): Max size of log files in bytes, default is 5 MB.
        - `log_backup_count` (int): Number of backup log files, default is 5.
        - `enable_console` (bool): Enable console logging, default is True.
        - `enable_file` (bool): Enable file logging, default is True.

    **Overrides:**
        - Environment variables can override the default and JSON file settings:
          - `LOG_LEVEL`, `LOG_DIR`, `LOG_MAX_BYTES`, `LOG_BACKUP_COUNT`,
            `ENABLE_CONSOLE_LOGGING`, `ENABLE_FILE_LOGGING`.
    """

    config = get_default_config()
    if config_file and os.path.exists(config_file):
        with open(config_file, "r") as f:
            json_config = json.load(f)
            config.update(json_config)

    """
    Example variables:
        LOG_LEVEL: Sets the logging level (e.g., DEBUG, INFO).
        LOG_DIR: Specifies the log file directory.
        LOG_MAX_BYTES: Configures the maximum size of log files.
        LOG_BACKUP_COUNT: Configures how many backup log files to retain.
        ENABLE_CONSOLE_LOGGING: Enables or disables console logging.
        ENABLE_FILE_LOGGING: Enables or disables file logging
    """
    config["log_level"] = os.getenv("LOG_LEVEL", config["log_level"]).upper()


    log_dir_extened = os.getenv("LOG_DIR", config["log_dir_extened"]) or ""
    if log_dir_extened:
        config["log_dir_extened"] = log_dir_extened
        log_dir_pwd = config["log_dir_pwd"]
        log_dir_path = os.path.join(log_dir_pwd, log_dir_extened)
        config["log_dir_path"] = log_dir_path

    config["log_max_bytes"] = int(os.getenv("LOG_MAX_BYTES", config["log_max_bytes"]))
    config["log_backup_count"] = int(
        os.getenv("LOG_BACKUP_COUNT", config["log_backup_count"])
    )
    config["enable_console"] = (
        os.getenv("ENABLE_CONSOLE_LOGGING", str(config["enable_console"])).lower()
        == "true"
    )
    config["enable_file"] = (
        os.getenv("ENABLE_FILE_LOGGING", str(config["enable_file"])).lower() == "true"
    )
    validate_config(config)

    return config


def validate_config(config):
    """
    Validate the logging configuration.

    :param config: The logging configuration dictionary to validate.
    :type config: dict

    :raises ValueError: If any required key is missing or a value is invalid.

    **Validation Checks:**
        - All required keys must be present: `log_level`, `log_dir`, `log_max_bytes`,
          `log_backup_count`, `enable_console`, `enable_file`.
        - `log_level` must be one of ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"].
        - `log_max_bytes` must be a positive integer.
        - `log_backup_count` must be an integer less than or equal to 100.
        - `log_dir` must be a valid and existing directory.
    """
    required_keys = [
        "log_level",
        "log_dir_pwd",
        "log_dir_extened",
        "log_dir_path",
        "log_max_bytes",
        "log_backup_count",
        "enable_console",
        "enable_file",
    ]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")

    if config["log_level"] not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError(f"Invalid log level: {config['log_level']}")

    if not isinstance(config["log_max_bytes"], int) or config["log_max_bytes"] <= 0:
        raise ValueError("log_max_bytes must be a positive integer.")

    if not isinstance(config["log_backup_count"], int):
        raise ValueError("log_backup_count must be an integer.")

    if config["log_backup_count"] > 100:
        raise ValueError("log_backup_count exceeds the maximum limit of 100.")

    try:
        os.makedirs(config["log_dir_path"], exist_ok=True)
    except Exception as e:
        raise ValueError(
            f"Failed to create log_dir_path '{config['log_dir_path']}': {e}"
        )

    if not os.path.isdir(config["log_dir_path"]):
        raise ValueError(
            f"log_dir_path must be a valid directory: {config['log_dir_path']}"
        )


class AsyncRotatingFileHandler(RotatingFileHandler):
    """
    Custom asynchronous rotating file handler for logging using a background thread.

    :param buffer_size: Number of log messages to batch before writing to the file. Default is 1.
    :type buffer_size: int
    :param debug_messages: Enable debug messages for debugging the handler's behavior.
    :type debug_messages: bool
    """

    """
    Custom asynchronous rotating file handler for logging using a background thread.

    Summary of the Workflow
        The constructor initializes all the necessary components for asynchronous logging.
        Log messages are enqueued into self.queue when the emit() method is called.
        The background worker thread (self.worker) processes messages from the queue and writes them to the file in batches defined by self.buffer_size.
        This setup ensures non-blocking log writing and efficient handling of file I/O operations.

    Asynchronous Logging Workflow
        emit() adds a log message to the queue.
        The background thread dequeues messages in _process_queue().
        Messages are written in batches to improve performance.
        The handler ensures all pending messages are written before shutting down.
    """

    def __init__(self, *args, buffer_size=1, debug_messages=False, **kwargs):
        """
        Initialize the asynchronous rotating file handler.

        :param args: Positional arguments for the base `RotatingFileHandler`.
        :param buffer_size: Number of log messages to batch before writing to the file. Default is 1.
        :type buffer_size: int
        :param debug_messages: Enable debug messages for debugging the handler's behavior.
        :type debug_messages: bool
        :param kwargs: Keyword arguments for the base `RotatingFileHandler`.
        """
        super().__init__(*args, **kwargs)
        self.debug_messages = debug_messages
        if self.debug_messages:
            print(
                f"AsyncRotatingFileHandler initialized with file: {self.baseFilename}"
            )
        self.buffer_size = buffer_size
        self.queue = queue.Queue()
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()
        self._closed = False

    def _debug(self, message):
        if self.debug_messages:
            print(message)

    def emit(self, record):
        """
        Enqueue a log record for asynchronous processing.

        :param record: The log record to enqueue.
        :type record: logging.LogRecord
        """

        """
        Override emit to enqueue the formatted record instead of writing it immediately.

        Key Features of This Method:
            - Asynchronous Behavior:
                By enqueueing messages, the main thread avoids being blocked by potentially slow file I/O operations.
                Writing to the log file is handled in a separate thread, improving the application's responsiveness.
            - Thread Safety:
                Using a thread-safe queue (self.queue) ensures that log messages can be safely added to the queue from multiple threads.
            - Error Resilience:
                The try-except block ensures that issues during logging do not crash the application. Errors are gracefully handled using handleError.
            - Debugging Support:
                The debug statements provide insights into the flow of log messages through the handler, which is useful during development.
        """
        self._debug("function emit")
        try:
            if self._stop_event.is_set():
                return

            self.queue.put_nowait(record)
            self._debug(f"Enqueued LogRecord: {record.getMessage()}")

        except Exception as e:
            self._debug(f"Error in emit: {e}")
            self.handleError(record)

    def _process_queue(self):
        """
        Process log messages from the queue in a background thread.

        **Workflow:**
            - Continuously dequeues log messages until the stop event is set.
            - Writes messages to the log file in batches.
        """

        buffer = []
        self._debug("function _process_queue")
        self._debug("Background thread started")

        while not self._stop_event.is_set() or not self.queue.empty():
            try:
                record = self.queue.get(timeout=0.1)
                if record is None:
                    continue
                buffer.append(record)
                self._debug(
                    f"\nDequeued log message: \n{record.getMessage()}"
                )

                if len(buffer) >= self.buffer_size:
                    self._debug(f"Buffer size: {len(buffer)}")
                    self._write_buffer(buffer)
                    buffer.clear()
            except queue.Empty:
                self._debug("Queue is empty")
                if buffer:
                    self._write_buffer(buffer)
                    buffer.clear()
            except Exception as e:
                self._debug(f"Error in _process_queue: {e}")
                pass

        if buffer:
            self._debug(f"Writing remaining messages: {len(buffer)}")
            self._write_buffer(buffer)
        self._debug("Background thread exiting")





    def _write_buffer(self, buffer):
        try:
            with self._lock:
                for record in buffer:
                    if self.shouldRollover(record):
                        self.doRollover()

                    msg = self.format(record)
                    self.stream.write(msg + "\n")

                self.flush()

        except Exception:
            for record in buffer:
                self.handleError(record)

    def close(self):
        """
        Safely close the logging handler.

        **Workflow:**
            - Writes all pending log messages in the queue to the file.
            - Ensures the background thread exits cleanly.
            - Calls the base class's close method.
        """

        """
        Key Features of the close Method:
            - Thread Safety:
                Uses a lock (self._lock) to ensure the closure process is safe in multi-threaded environments.
            - Graceful Shutdown:
                Signals the background thread to stop using self._stop_event.
                Ensures the thread finishes processing before shutting down completely.
            - Processing Remaining Messages:
                Checks for any remaining messages in the queue and writes them to the file to prevent data loss.
            - Integration with Parent Class:
                Calls the parent class’s close method to ensure proper cleanup of resources.
            - Idempotence:
                Ensures that calling close multiple times has no adverse effects by checking the self._closed flag.
        """
        with self._lock:
            self._debug("function close")
            if not self._closed:
                self._closed = True
                self._debug("Closing AsyncRotatingFileHandler")

                self._stop_event.set()

                try:
                    self.queue.put_nowait(None)
                except Exception:
                    pass

                self.worker.join(timeout=2.0)

                if self.worker.is_alive():
                    self._debug(
                        "Worker still alive; skipping stream close to avoid closed-file writes"
                    )
                    return

                buffer = []
                while True:
                    try:
                        item = self.queue.get_nowait()
                    except queue.Empty:
                        break
                    if item is None:
                        continue
                    buffer.append(item)

                if buffer:
                    self._write_buffer(buffer)

                super().close()
                self._debug("AsyncRotatingFileHandler closed")


def setup_logger(logger_name=None, config_file=None, debug_messages=False):
    """
    Set up a named logger with asynchronous file logging and dynamic configuration.

    :param logger_name: Name of the logger. Defaults to the module name if None.
    :type logger_name: str, optional
    :param config_file: Path to a JSON configuration file for logging.
    :type config_file: str, optional
    :param debug_messages: Enable debug messages during logger setup.
    :type debug_messages: bool

    :return: A configured logger instance.
    :rtype: logging.Logger
    """

    """
    Set up a named logger with asynchronous file logging and dynamic configuration.
    """

    def _debug(message):
        """
        Print debug messages if debug_messages is enabled.
        """
        if debug_messages:
            print(message)

    _debug("function setup_logger")

    config = load_config(config_file)

    log_dir_path = config["log_dir_path"]
    log_file_name = os.getenv("LOG_FILE_NAME", "reportlog.log")

    log_file = os.path.join(log_dir_path, log_file_name)

    _debug(f"Log directory: {log_dir_path}")
    _debug(f"Log file absolute path: {log_file}")

    logger = logging.getLogger(logger_name or __name__)


    if logger.hasHandlers():
        for handler in logger.handlers[:]:
            try:
                handler.close()
            except Exception:
                pass
            logger.removeHandler(handler)
        _debug("Cleared existing handlers")

    logger.setLevel(getattr(logging, config["log_level"], logging.INFO))
    logger.propagate = False
    if config["enable_console"]:
        if hasattr(sys.stdout, "reconfigure"):
            try:
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        console_handler.setLevel(getattr(logging, config["log_level"], logging.INFO))

        logger.addHandler(console_handler)
        _debug(
            "Added StreamHandler for console logging with UTF-8 encoding"
        )

    if config["enable_file"]:
        try:
            file_handler = AsyncRotatingFileHandler(
                log_file,
                maxBytes=config["log_max_bytes"],
                backupCount=config["log_backup_count"],
                buffer_size=1,
                encoding="utf-8",
            )
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s %(levelname)s %(name)s:%(lineno)d [%(threadName)s] %(message)s"
                )
            )
            logger.addHandler(file_handler)
            _debug(f"AsyncRotatingFileHandler added: {log_file}")
        except Exception as file_error:
            logger.warning(
                "File logging failed: %s. Falling back to console-only logging.",
                file_error,
            )
            _debug(
                f"Failed to add AsyncRotatingFileHandler: {file_error}"
            )
    return logger


@contextmanager
def managed_logger(logger_name=None, config_file=None):
    """
    Context manager for a logger with automatic cleanup.

    :param logger_name: Name of the logger.
    :type logger_name: str, optional
    :param config_file: Path to a JSON configuration file for logging.
    :type config_file: str, optional

    :yield: A configured logger instance.
    :rtype: logging.Logger

    **Example:**
        >>> with managed_logger("my_logger", "config.json") as logger:
        >>>     logger.info("Log message")
    """

    """
    Why Use managed_logger: It simplifies logger management, ensures proper cleanup,
    and integrates seamlessly with Python's with statement for clean and readable code.

    Best Practice: Use managed_logger for temporary loggers or in scenarios where
    automatic cleanup is critical. For long-lived applications,
    a persistent logger configured at startup may be more appropriate.
    """
    logger = setup_logger(logger_name, config_file)
    try:
        yield logger
    finally:
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)
        logging.shutdown()
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/path_utils.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/path_utils.py
from pathlib import Path


def validate_path(var_path: Path) -> Path:
    """
    Validate a filesystem path and return the resolved directory path.

    :param var_path: Path to validate.
    :type var_path: Path
    :return: Resolved directory path.
    :rtype: Path
    :raises ValueError: If the path does not exist or is not a directory.
    """
    resolved_path = var_path.expanduser().resolve()

    if not resolved_path.exists():
        raise ValueError(f"Start path does not exist: {resolved_path}")

    if not resolved_path.is_dir():
        raise ValueError(f"Start path is not a directory: {resolved_path}")

    return resolved_path
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/token_usage.py BELOW:
########################################

```python
# src/generate_file_structure/my_utils/token_usage.py
import json
import signal
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from generate_file_structure.my_utils.env_loader import load_dotenv_once


class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton.
    """

    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class TokenUsage(metaclass=SingletonMeta):
    """
    Singleton class to manage and persist token usage across threads.
    """

    TOKEN_FILE = "token_usage_tier.json"

    RATE_LIMITS = {
        "Free": {
            "gpt-4o-mini": {"RPM": 3, "TPM": 40000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 100,
                "TPM": 2000,
                "Batch Queue Limit": 40000,
            },
            "text-embedding-3-small": {
                "RPM": 100,
                "TPM": 2000,
                "Batch Queue Limit": 40000,
            },
            "text-embedding-ada-002": {
                "RPM": 100,
                "TPM": 2000,
                "Batch Queue Limit": 40000,
            },
            "omni-moderation-*": {"RPM": 250, "TPM": 5000, "Batch Queue Limit": "-"},
            "whisper-1": {"RPM": 3, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 3, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 5, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 1, "TPM": "-", "Batch Queue Limit": "-"},
        },
        "Tier 1": {
            "gpt-4o": {"RPM": 500, "TPM": 30000, "Batch Queue Limit": 90000},
            "gpt-4o-mini": {"RPM": 500, "TPM": 200000, "Batch Queue Limit": 2000000},
            "gpt-4o-realtime-preview": {
                "RPM": 100,
                "TPM": 20000,
                "Batch Queue Limit": "-",
            },
            "o1-preview": {"RPM": 500, "TPM": 30000, "Batch Queue Limit": 90000},
            "o1-mini": {"RPM": 500, "TPM": 200000, "Batch Queue Limit": 2000000},
            "gpt-4-turbo": {"RPM": 500, "TPM": 30000, "Batch Queue Limit": 90000},
            "gpt-4": {"RPM": 500, "TPM": 10000, "Batch Queue Limit": 100000},
            "gpt-3.5-turbo": {
                "RPM": 3500,
                "TPM": 2000000,
                "Batch Queue Limit": 5000000,
            },
            "omni-moderation-*": {"RPM": 500, "TPM": 10000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 3000,
                "TPM": 1000000,
                "Batch Queue Limit": 3000000,
            },
            "text-embedding-3-small": {
                "RPM": 3000,
                "TPM": 1000000,
                "Batch Queue Limit": 3000000,
            },
            "text-embedding-ada-002": {
                "RPM": 3000,
                "TPM": 1000000,
                "Batch Queue Limit": 3000000,
            },
            "whisper-1": {"RPM": 500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1-hd": {"RPM": 500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 500, "TPM": "-", "Batch Queue Limit": "-"},
        },
        "Tier 2": {
            "gpt-4o": {"RPM": 5000, "TPM": 450000, "Batch Queue Limit": 1350000},
            "gpt-4o-mini": {"RPM": 5000, "TPM": 2000000, "Batch Queue Limit": 20000000},
            "gpt-4o-realtime-preview": {
                "RPM": 200,
                "TPM": 40000,
                "Batch Queue Limit": "-",
            },
            "o1-preview": {"RPM": 5000, "TPM": 450000, "Batch Queue Limit": 1350000},
            "o1-mini": {"RPM": 5000, "TPM": 2000000, "Batch Queue Limit": 20000000},
            "gpt-4-turbo": {"RPM": 5000, "TPM": 450000, "Batch Queue Limit": 1350000},
            "gpt-4": {"RPM": 5000, "TPM": 40000, "Batch Queue Limit": 200000},
            "gpt-3.5-turbo": {
                "RPM": 3500,
                "TPM": 2000000,
                "Batch Queue Limit": 5000000,
            },
            "omni-moderation-*": {"RPM": 500, "TPM": 20000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 5000,
                "TPM": 1000000,
                "Batch Queue Limit": 20000000,
            },
            "text-embedding-3-small": {
                "RPM": 5000,
                "TPM": 1000000,
                "Batch Queue Limit": 20000000,
            },
            "text-embedding-ada-002": {
                "RPM": 5000,
                "TPM": 1000000,
                "Batch Queue Limit": 20000000,
            },
            "whisper-1": {"RPM": 2500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 2500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1-hd": {"RPM": 2500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 2500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 2500, "TPM": "-", "Batch Queue Limit": "-"},
        },
        "Tier 3": {
            "gpt-4o": {"RPM": 5000, "TPM": 800000, "Batch Queue Limit": 50000000},
            "gpt-4o-mini": {"RPM": 5000, "TPM": 4000000, "Batch Queue Limit": 40000000},
            "gpt-4o-realtime-preview": {
                "RPM": 5000,
                "TPM": 400000,
                "Batch Queue Limit": "-",
            },
            "o1-preview": {"RPM": 5000, "TPM": 800000, "Batch Queue Limit": 50000000},
            "o1-mini": {"RPM": 5000, "TPM": 4000000, "Batch Queue Limit": 40000000},
            "gpt-4-turbo": {"RPM": 5000, "TPM": 600000, "Batch Queue Limit": 40000000},
            "gpt-4": {"RPM": 5000, "TPM": 80000, "Batch Queue Limit": 5000000},
            "gpt-3.5-turbo": {
                "RPM": 3500,
                "TPM": 4000000,
                "Batch Queue Limit": 100000000,
            },
            "omni-moderation-*": {"RPM": 1000, "TPM": 50000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 5000,
                "TPM": 5000000,
                "Batch Queue Limit": 100000000,
            },
            "text-embedding-3-small": {
                "RPM": 5000,
                "TPM": 5000000,
                "Batch Queue Limit": 100000000,
            },
            "text-embedding-ada-002": {
                "RPM": 5000,
                "TPM": 5000000,
                "Batch Queue Limit": 100000000,
            },
            "whisper-1": {"RPM": 5000, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 5000, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1-hd": {"RPM": 5000, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 5000, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 5000, "TPM": "-", "Batch Queue Limit": "-"},
        },
        "Tier 4": {
            "gpt-4o": {"RPM": 10000, "TPM": 2000000, "Batch Queue Limit": 200000000},
            "gpt-4o-mini": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 1000000000,
            },
            "gpt-4o-realtime-preview": {
                "RPM": 10000,
                "TPM": 2000000,
                "Batch Queue Limit": "-",
            },
            "o1": {"RPM": 1000, "TPM": 30000000, "Batch Queue Limit": "-"},
            "o1-preview": {
                "RPM": 10000,
                "TPM": 30000000,
                "Batch Queue Limit": 5000000000,
            },
            "o1-mini": {
                "RPM": 30000,
                "TPM": 150000000,
                "Batch Queue Limit": 15000000000,
            },
            "gpt-4-turbo": {
                "RPM": 10000,
                "TPM": 2000000,
                "Batch Queue Limit": 300000000,
            },
            "gpt-4": {"RPM": 10000, "TPM": 1000000, "Batch Queue Limit": 150000000},
            "gpt-3.5-turbo": {
                "RPM": 10000,
                "TPM": 50000000,
                "Batch Queue Limit": 10000000000,
            },
            "omni-moderation-*": {"RPM": 5000, "TPM": 500000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "text-embedding-3-small": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "text-embedding-ada-002": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "whisper-1": {"RPM": 7500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 7500, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1-hd": {"RPM": 7500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 7500, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 7500, "TPM": "-", "Batch Queue Limit": "-"},
        },
        "Tier 5": {
            "gpt-4o": {"RPM": 10000, "TPM": 30000000, "Batch Queue Limit": 5000000000},
            "gpt-4o-mini": {
                "RPM": 30000,
                "TPM": 150000000,
                "Batch Queue Limit": 15000000000,
            },
            "gpt-4o-realtime-preview": {
                "RPM": 20000,
                "TPM": 10000000,
                "Batch Queue Limit": "-",
            },
            "o1": {"RPM": 1000, "TPM": 30000000, "Batch Queue Limit": "-"},
            "o1-preview": {
                "RPM": 10000,
                "TPM": 30000000,
                "Batch Queue Limit": 5000000000,
            },
            "o1-mini": {
                "RPM": 30000,
                "TPM": 150000000,
                "Batch Queue Limit": 15000000000,
            },
            "gpt-4-turbo": {
                "RPM": 10000,
                "TPM": 2000000,
                "Batch Queue Limit": 300000000,
            },
            "gpt-4": {"RPM": 10000, "TPM": 1000000, "Batch Queue Limit": 150000000},
            "gpt-3.5-turbo": {
                "RPM": 10000,
                "TPM": 50000000,
                "Batch Queue Limit": 10000000000,
            },
            "omni-moderation-*": {"RPM": 5000, "TPM": 500000, "Batch Queue Limit": "-"},
            "text-embedding-3-large": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "text-embedding-3-small": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "text-embedding-ada-002": {
                "RPM": 10000,
                "TPM": 10000000,
                "Batch Queue Limit": 4000000000,
            },
            "whisper-1": {"RPM": 10000, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1": {"RPM": 10000, "TPM": "-", "Batch Queue Limit": "-"},
            "tts-1-hd": {"RPM": 10000, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-2": {"RPM": 10000, "TPM": "-", "Batch Queue Limit": "-"},
            "dall-e-3": {"RPM": 10000, "TPM": "-", "Batch Queue Limit": "-"},
        },
    }

    def __new__(cls, *args, **kwargs):
        return super(TokenUsage, cls).__new__(cls)

    def __init__(self):
        self.lock = threading.Lock()
        self.reset_time = time.time() + 60
        self.current_tier = None
        self.current_model = None
        self.tpm = 0
        self.remaining_tokens = 0
        self.batch_queue_limit = "-"
        self.shutdown_event = threading.Event()
        self.load_config()
        self.start_reset_thread()
        self.setup_signal_handlers()

    def load_config(self):
        """
        Load the tier and model from TOKEN_FILE and set TPM accordingly.
        """
        try:
            load_dotenv_once()
        except Exception:
            pass

        config_path = Path(__file__).parent / self.TOKEN_FILE

        if not config_path.exists():
            raise FileNotFoundError(
                f"{self.TOKEN_FILE} does not exist in {Path(__file__).parent}."
            )

        with open(config_path, "r") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON from {self.TOKEN_FILE}: {e}")

        self.current_tier = config.get("tier")
        self.current_model = config.get("model")

        if not self.current_tier or not self.current_model:
            raise ValueError("TOKEN_FILE must contain 'tier' and 'model'.")

        tier_limits = self.RATE_LIMITS.get(self.current_tier)
        if not tier_limits:
            raise ValueError(f"Tier '{self.current_tier}' is not defined.")

        model_limits = tier_limits.get(self.current_model)
        if not model_limits:
            raise ValueError(
                f"Model '{self.current_model}' is not defined in Tier '{self.current_tier}'."
            )

        self.tpm = model_limits["TPM"]
        self.batch_queue_limit = model_limits["Batch Queue Limit"]

        if isinstance(self.tpm, str) and self.tpm == "-":
            self.tpm = 0

        self.remaining_tokens = self.tpm
        print(
            f"[{datetime.now(timezone.utc)}] Loaded configuration: Tier={self.current_tier}, Model={self.current_model}, TPM={self.tpm}"
        )

    def update_tokens(self, tokens_used):
        """
        Decrease the remaining_tokens by tokens_used.
        """
        with self.lock:
            if tokens_used > self.remaining_tokens:
                raise ValueError("Insufficient tokens remaining.")
            self.remaining_tokens -= tokens_used
            print(
                f"[{datetime.now(timezone.utc)}] Tokens used: {tokens_used}. Remaining tokens: {self.remaining_tokens}"
            )

    def get_remaining_tokens(self):
        """
        Return the number of remaining tokens.
        """
        with self.lock:
            return self.remaining_tokens

    def reset_tokens(self):
        """
        Reset remaining_tokens to tpm and restart the reset timer.
        """
        with self.lock:
            self.remaining_tokens = self.tpm
            self.reset_time = time.time() + 60
            print(
                f"[{datetime.now(timezone.utc)}] Tokens have been reset. Remaining tokens: {self.remaining_tokens}"
            )

    def display_info(self):
        """
        Return the current model, tier, and TPM.
        """
        with self.lock:
            return {
                "Tier": self.current_tier,
                "Model": self.current_model,
                "TPM": self.tpm,
                "Remaining Tokens": self.remaining_tokens,
                "Batch Queue Limit": self.batch_queue_limit,
            }

    def start_reset_thread(self):
        """
        Start a background thread that resets tokens every 60 seconds.
        """
        reset_thread = threading.Thread(
            target=self._reset_tokens_periodically, daemon=True
        )
        reset_thread.start()

    def _reset_tokens_periodically(self):
        """
        Background thread to reset tokens at every reset_time.
        """
        while not self.shutdown_event.is_set():
            current_time = time.time()
            sleep_duration = self.reset_time - current_time
            if sleep_duration > 0:
                shutdown = self.shutdown_event.wait(timeout=sleep_duration)
                if shutdown:
                    break
            self.reset_tokens()

    def shutdown(self):
        """
        Signal the background thread to terminate gracefully.
        """
        self.shutdown_event.set()
        print(
            f"[{datetime.now(timezone.utc)}] Shutdown signal received. Terminating TokenUsage."
        )

    def setup_signal_handlers(self):
        """
        Setup signal handlers to gracefully shutdown on termination signals.
        """
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)

    def handle_signal(self, signum, frame):
        """
        Handle incoming termination signals by initiating a graceful shutdown.
        """
        print(
            f"[{datetime.now(timezone.utc)}] Received signal {signum}. Initiating graceful shutdown."
        )
        self.shutdown()
```

########################################
Here is my code for generate_file_structure/src/generate_file_structure/my_utils/token_usage_tier.json BELOW:
########################################

```json
{
  "tier": "Tier 3",
  "model": "gpt-4o"
}
```

########################################
Here is my code for generate_file_structure/tests/__init__.py BELOW:
########################################

```python
```
