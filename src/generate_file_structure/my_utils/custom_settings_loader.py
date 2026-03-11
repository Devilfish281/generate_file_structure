# src/generate_file_structure/my_utils/custom_settings_loader.py
import re
import threading
from pathlib import Path

_CUSTOM_SETTINGS_CACHE = None
_CUSTOM_SETTINGS_LOCK = threading.Lock()

_SETTING_LINE_PATTERN = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*(.*?)\s*$")


def _clean_value(raw_value: str) -> str:
    """Normalize a parsed value from `Custom_setting.md`."""
    value = raw_value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def load_custom_settings_once(custom_settings_path: Path) -> dict[str, str]:
    """
    Read `Custom_setting.md` exactly once per process and return parsed key/value overrides.
    Only lines that match `KEY=VALUE` are loaded.
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
                match = _SETTING_LINE_PATTERN.match(line)
                if not match:
                    continue
                key, raw_value = match.groups()
                parsed_settings[key] = _clean_value(raw_value)

        _CUSTOM_SETTINGS_CACHE = parsed_settings
        return dict(_CUSTOM_SETTINGS_CACHE)
