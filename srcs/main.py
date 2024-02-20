import os
import sys
import socket
import flags
import colorama
import time
import random
from commands import clear, exit, cat, cd, cron, ls, misc, spmn, mkdir
from misc import misc



def main():
    arguments = sys.argv
    banner = """
    _____        _____ _          _ _ 
    |  _ \ _   _/ ___|| |__   ___| | |
    | |_) | | | \___ \| '_ \ / _ \ | |
    |  __/| |_| |___) | | | |  __/ | |
    |_|    \__, |____/|_| |_|\___|_|_|   
            |___/                         
    ==================================
    @  Version: 1.0.0 - INovomiast   @
    ==================================
    """
    
    # Clear console
    if sys.platform == "win32":
        os.system('cls')
    elif sys.platform == "darwin" or sys.platform == "linux":
        os.system('clear')

    # Load modules
    time.sleep(0.5)
    print(banner)
    time.sleep(1)
    print("Starting PyShell 1.0.0...")
    time.sleep(0.5)
    misc.load_modules(os.path.join(os.getcwd(), "../modules"))
    time.sleep(1)
    clear.clear_shell()
    print(banner)

    # Prompt to insert command      
    preInputString = f"{colorama.Fore.LIGHTBLUE_EX}\ue62a{colorama.Fore.RESET} [{colorama.Fore.GREEN}{os.getlogin()}{colorama.Fore.RESET}\\/{colorama.Fore.LIGHTRED_EX}{socket.gethostname()}{colorama.Fore.RESET}]{colorama.Fore.LIGHTYELLOW_EX}$->{colorama.Fore.RESET} "
    while True:
        cmnd = input(preInputString) # Where the command is stored

        if cmnd == "clear":
            clear.clear_shell()
        elif cmnd == "exit":
            exit.exit_shell()
        elif cmnd == "ls":
            ls.list_directory()
        elif cmnd == "ls -la":
            ls.list_all_directory()
        elif cmnd.startswith('cd'):
            cd.change_dir(cmnd)
        elif cmnd.startswith('cat'):
            cat.parse_file(cmnd)
        elif cmnd.startswith('ssh'):
            pass
        elif cmnd.startswith('spmn'):
            spmn.supermenu()
        elif cmnd == "reload":
            misc.misc_commands.reload()
        elif cmnd.startswith("cron"):
            cron.cron_cmnd(cmnd)
        elif cmnd.startswith("mkdir"):
            mkdir.makedir(cmnd)
        elif cmnd.startswith("rm"):
            cmd_flags = flags.parseFlags(cmnd)
            
            if not flags.checkFlags(cmd_flags, "rm <file>"):
                pass
            
            if flags.checkFlags(cmd_flags) == True:
                try:
                    os.system(f"rm -r {os.path.join(os.getcwd(), cmd_flags[0])}") # PARTIAL FIX: Puede haber problemas de compatibilidad.
                    print(f"{cmd_flags[0]}: removed successfully!")
                except FileNotFoundError:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {cmd_flags[0]} not found!")
                except PermissionError as e:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {e}!")
                    
        else:
            print(f"'{cmnd}' does not exists or theres a typo or is not installed as a module.")
            print(f"Check and re-run it!")
            print(f"pypkg <package-name> to install the module!")
            


if __name__ == "__main__":
    main()