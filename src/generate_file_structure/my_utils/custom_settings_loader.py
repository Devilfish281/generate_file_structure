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
