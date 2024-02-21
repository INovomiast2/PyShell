import os
import sys
import socket
from utils import colors

class execute:
    def __init__(self, command="", flags=""):
        excluded_commands = {'clear', 'ls', 'ls -la', 'chdr'}
        if command.startswith('cd ') or command in excluded_commands:  # Check for 'cd ' prefix
            pass
        else:
            os.system(command)

