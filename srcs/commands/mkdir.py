import os
import sys
import time
import flags

def makedir(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags):
        print("mkdir <name>")
        return 0
    
    if flags.checkFlags(command_flags):
        try:
            print(f"Creating {command_flags[0]}...")
            time.sleep(1)
            os.mkdir(command_flags[0])
            return 0
        except FileExistsError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {command_flags[1]} already exists!")
            return 1