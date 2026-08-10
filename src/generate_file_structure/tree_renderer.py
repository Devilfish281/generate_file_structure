from pathlib import Path  # Added Code


def render_directory_tree(  # Added Code
    root_dir: Path,  # Added Code
    children_by_directory: dict[Path, list[Path]],  # Added Code
) -> list[str]:  # Added Code
    """Render one structurally correct Unicode directory tree."""  # Added Code
    root_dir = root_dir.resolve()  # Added Code
    lines = [f"{root_dir}/\n"]  # Added Code

    def walk(directory: Path, prefix: str) -> None:  # Added Code
        entries = children_by_directory.get(directory, [])  # Added Code

        for index, entry in enumerate(entries):  # Added Code
            is_last = index == len(entries) - 1  # Added Code
            branch = "└── " if is_last else "├── "  # Added Code
            suffix = "/" if entry.is_dir() else ""  # Added Code
            lines.append(f"{prefix}{branch}{entry.name}{suffix}\n")  # Added Code

            if entry.is_dir():  # Added Code
                child_prefix = prefix + ("    " if is_last else "│   ")  # Added Code
                walk(entry, child_prefix)  # Added Code

    walk(root_dir, "")  # Added Code
    return lines  # Added Code
