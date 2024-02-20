import sys
import os

def clear_shell():
    if sys.platform == 'darwin' or sys.platform == 'linux':
        os.system('clear')
        return 0
    else:
        os.system('cls')
        return 0
    return 1