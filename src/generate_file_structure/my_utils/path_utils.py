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
