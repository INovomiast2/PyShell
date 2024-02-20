import os
import time
import subprocess
import sys

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
    Checks for changes in the current file and restarts the main script if necessary.
    Handles potential missing directory errors.
    """
    try:
        last_mtime = os.path.getmtime(".")
        while True:
            time.sleep(0.5)  # Check for changes every 5 seconds
            current_mtime = os.path.getmtime(sys.argv[1])
            if current_mtime != last_mtime:
                last_mtime = current_mtime
                print("File changed, restarting main script...")
                run_main_script()
    except FileNotFoundError as e:
        print(f"Error: Could not access working directory! ({e})")

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
