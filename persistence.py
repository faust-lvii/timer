# persistence.py
import json
import os
import time
from pathlib import Path
import msvcrt
import tempfile

REMINDERS_FILE = Path(os.path.dirname(os.path.abspath(__file__))) / "reminders.json"

def load_reminders():
    try:
        if not REMINDERS_FILE.exists():
            return []

        # Try to open and read the file
        try:
            with open(REMINDERS_FILE, "r") as f:
                # Try to acquire a lock
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                try:
                    data = json.load(f)
                    # Validate data structure
                    if not isinstance(data, list):
                        print("Warning: Invalid data structure in reminders file")
                        return []
                    return data
                finally:
                    # Release the lock
                    f.seek(0)
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
        except (IOError, OSError) as e:
            print(f"Could not acquire lock: {str(e)}")
            # If we can't get a lock, just try to read the file
            with open(REMINDERS_FILE, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return data
    except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
        print(f"Error loading reminders: {str(e)}")
        return []
    except Exception as e:
        print(f"Unexpected error loading reminders: {str(e)}")
        return []

def save_reminders(reminders):
    if not isinstance(reminders, list):
        raise ValueError("Reminders must be a list")

    try:
        # Ensure directory exists
        REMINDERS_FILE.parent.mkdir(parents=True, exist_ok=True)

        # Create a temporary file in the same directory
        temp_fd, temp_path = tempfile.mkstemp(dir=str(REMINDERS_FILE.parent), text=True)
        try:
            with os.fdopen(temp_fd, 'w') as temp_file:
                # Write the data to the temporary file
                json.dump(reminders, temp_file, indent=2)
            
            # On Windows, we need to remove the target file first
            try:
                REMINDERS_FILE.unlink()
            except FileNotFoundError:
                pass
            
            # Rename temporary file to target file
            os.rename(temp_path, REMINDERS_FILE)
        except Exception as e:
            # Clean up the temporary file if something goes wrong
            try:
                os.unlink(temp_path)
            except OSError:
                pass
            raise e
    except Exception as e:
        print(f"Error saving reminders: {str(e)}")
        raise