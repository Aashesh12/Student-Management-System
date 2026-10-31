import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load student records from JSON."""

    try:
        if not DATA_FILE.exists():
            return []

        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not read student data: {error}")
        return []


def save_students(students):
    """Save student records to JSON."""

    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError as error:
        print(f"Error: Could not save student data: {error}")
        return False