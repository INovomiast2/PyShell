import sys
import os

def clear_shell():
    if sys.platform == 'darwin' or sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')