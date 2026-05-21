def generate_file_structure():
    """
    Generates the directory structure of the given root directory and collects .py files.

    :return: Tuple containing list of directory structure lines and list of .py file paths.
    :rtype: tuple[list[str], list[Path]]
    """
    lines = ["The File structure for my program is BELOW:\n"]
    py_files_list = []
    root_dir = setup_config.start_dir  # Changed Code
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
            for child in dirs[:]:  # Changed Code
                child_path = root_path / child  # Added Code
                if not child_path.is_dir():  # Changed Code
                    continue  # Changed Code

                if child == "tests" and setup_config.include_tests_flag:  # Changed Code
                    continue  # Changed Code

                while True:
                    response = (
                        input(
                            f"Do you want to include the directory '{child}'? (y/n): "  # Changed Code
                        )
                        .strip()
                        .lower()
                    )
                    if response in {"y", "n"}:
                        break
                    logger.info("Invalid input. Please enter 'y' or 'n'.")

                if response == "y":
                    continue  # Changed Code
                else:
                    dirs.remove(child)  # Added Code
                    excluded_dirs.add(child)  # Changed Code
                    logger.info(f"Excluded directory: {child}")  # Changed Code
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
            sub_indent = indent + "    "

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
