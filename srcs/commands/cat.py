import os
import sys
import colorama
import flags

def parse_file(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags, "Usage: cat <file>"):
        pass
    
    if command_flags[0] == "--help":
        print("Usage: cat <file>")
        print("Prints the content of a file.")
        print("Example: cat file.txt")
    else:
        try:
            with open(os.path.join(os.getcwd(), command_flags[0]), "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{command_flags[0]}` not found!")
        except FileExistsError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{command_flags[0]}` is a directory!")