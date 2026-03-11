# src/generate_file_structure/my_utils/directory_setup.py
import threading
from pathlib import Path

_DIRECTORY_INITIALIZED = False
_DIRECTORY_LOCK = threading.Lock()


def create_chat_gpt_directory_once(setup_config) -> bool:
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

    # Fast path: if already initialized, do nothing.
    if _DIRECTORY_INITIALIZED:
        return False

    with _DIRECTORY_LOCK:
        # Double-check inside the lock to avoid races.
        if _DIRECTORY_INITIALIZED:
            return False

        main_dir = getattr(setup_config, "get_program_output_dir", None)
        chunks_dir = getattr(setup_config, "get_chunks_dir", None)
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
