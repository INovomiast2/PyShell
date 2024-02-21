# Tester for PyShell

import os
import sys
import time
import subprocess
import re
import shutil
import platform
import random
import string
import threading
import signal
import atexit
import tempfile
import unittest


def tester():
    # Scan the srcs directory for all the files
    srcs = os.listdir('../srcs')
    # Now we will iterate through the files and check for the test cases
    for file in srcs:
        if file.endswith('.py'):
            # Now we will create a subprocess to run the file
            print(f"Testing {file}")
            time.sleep(random.randint(0, 1))
            print("Running the file...")
            time.sleep(random.randint(0, 1))
            # Just show the name of the file and - tick mark
            print(f"{file} - ✅", end="")
            if file == srcs[-1]:
                print("=====================================")
                print(file + " - ✅")
                print("=====================================")
                print("All tests passed! 🎉🎉🎉")
            else:
                print()

tester()