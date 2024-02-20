import os
import time
import random

class misc():
    def load_modules(directory):
        messages = []

        if len(os.listdir(directory)) <= 0:
            print("PyShell - No modules where found")
            pass

        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                module_name = os.path.splitext(filename)[0]
                messages.append(f"Loading module: {module_name} ")
            for msg in messages:
                print("PyShell - " + msg)
                time.sleep(random.random() * 0.2)  # Add random delay for each module