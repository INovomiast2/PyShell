import os
import time
import subprocess
import sys
from pathlib import Path
def run_main_script():
    """
    Executes the main script in the same directory using the Python interpreter.
    Handles potential file not found errors.
    """
    try:
        if len(sys.argv) == 2:
            subprocess.run(["python3", sys.argv[1]])
        elif len(sys.argv) == 3:
            subprocess.run(["python3", sys.argv[1], sys.argv[2]])
    except FileNotFoundError as e:
        print(f"Error: Main script 'main.py' not found! ({e})")
    except subprocess.CalledProcessError as e:
        print(f"Error running main script: {e}")

def monitor_for_changes():
    """
    Checks for changes in any file inside the project and restarts the main script if necessary.
    Handles potential missing directory errors.
    """
    try:
        project_path = Path(sys.argv[0]).resolve().parent
        last_mtime = {}
        while True:
            time.sleep(0.5)  # Check for changes every 0.5 seconds
            for root, _, files in os.walk(project_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    current_mtime = os.path.getmtime(file_path)
                    if file_path not in last_mtime:
                        last_mtime[file_path] = current_mtime
                    elif current_mtime != last_mtime[file_path]:
                        last_mtime[file_path] = current_mtime
                        print(f"File '{file_path}' changed, restarting main script...")
                        run_main_script()
    except FileNotFoundError as e:
        print(f"Error: Could not access project directory! ({e})")

def main():
    """
    Entry point for the process rerunner.
    Prints a message and starts monitoring for changes.
    """
    print("Starting process rerunner...")
    run_main_script()  # Run main.py initially
    monitor_for_changes()  # Start monitoring for changes

if __name__ == "__main__":
    main()
