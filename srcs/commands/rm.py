import os
import sys
import flags
import colorama

def remove(command):
    cmd_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(cmd_flags, "rm <file>"):
        return 0
    
    if flags.checkFlags(cmd_flags) == True:
        try:
            os.system(f"rm -r {os.path.join(os.getcwd(), cmd_flags[0])}") # PARTIAL FIX: Puede haber problemas de compatibilidad.
            print(f"{cmd_flags[0]}: removed successfully!")
            return 0
        except FileNotFoundError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {cmd_flags[0]} not found!")
            return 1
        except PermissionError as e:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {e}!")
            return 1