import sys
import os

def exit_shell():
    if sys.platform == 'darwin' or sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')
    sys.exit(0)