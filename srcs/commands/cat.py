import os
import sys
from utils import colors, help
import flags

def parse_file(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags, "Usage: cat <file>"):
        return 0
    
    if command_flags[0] == "--help":
        print(help.message.cat_help)
        return 0
    else:
        try:
            with open(os.path.join(os.getcwd(), command_flags[0]), "r", encoding="utf-8") as file:
                print(file.read())
            file.close()
            return 0
        except FileNotFoundError:
            print(f"{colors.RED}[ERROR]{colors.RESET}: `{command_flags[0]}` not found!")
            return 1
        except FileExistsError:
            print(f"{colors.RED}[ERROR]{colors.RESET}: `{command_flags[0]}` is a directory!")
            return 1