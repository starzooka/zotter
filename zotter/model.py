import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# -------------------------------------------------
# Storage locations
# -------------------------------------------------

NOTES_FILE: Path = Path.home() / ".zotter.json"
TRASH_FILE: Path = Path.home() / ".zotter_trash.json"


# -------------------------------------------------
# Models
# -------------------------------------------------

class Note:
    """
    Represents a single note entry in Zotter.

    Attributes:
        title (str): Short descriptive title of the note
        content (str): Full note content
        category (str): Logical category for grouping
        date (str): Creation timestamp (YYYY-MM-DD HH:MM)

    Example:
        >>> note = Note("Idea", "Build a CLI note app", "Projects")
        >>> note.title
        'Idea'
    """

    def __init__(self, title: str, content: str, category: str = "General"):
        self.title = title
        self.content = content
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")


# -------------------------------------------------
# Internal helpers
# -------------------------------------------------

def load_data(filepath: Path) -> List[Dict[str, Any]]:
    """
    Load JSON data from disk safely.

    If the file does not exist or is corrupted,
    an empty list is returned instead of raising errors.

    Args:
        filepath (Path): Path to the JSON file

    Returns:
        list[dict]: Loaded data
    """
    if not filepath.exists():
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(filepath: Path, data: List[Dict[str, Any]]) -> None:
    """
    Persist data to disk in JSON format.

    Args:
        filepath (Path): Destination file
        data (list[dict]): Data to write
    """
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# -------------------------------------------------
# Public API (used by the CLI)
# -------------------------------------------------

def load_notes() -> List[Dict[str, Any]]:
    """
    Load all active notes.

    Returns:
        list[dict]: Active notes
    """
    return load_data(NOTES_FILE)


def save_notes(notes: List[Dict[str, Any]]) -> None:
    """
    Save active notes to disk.

    Args:
        notes (list[dict]): Notes to persist
    """
    save_data(NOTES_FILE, notes)


def load_trash() -> List[Dict[str, Any]]:
    """
    Load all trashed notes.

    Returns:
        list[dict]: Deleted notes
    """
    return load_data(TRASH_FILE)


def save_trash(trash: List[Dict[str, Any]]) -> None:
    """
    Save trashed notes to disk.

    Args:
        trash (list[dict]): Trash items to persist
    """
    save_data(TRASH_FILE, trash)
