import os
import sys
import socket
from utils import colors
import time
import random
from commands import clear, exit, cat, cd, cron, ls, misc as mc, spmn, mkdir, rm, echo
from misc import misc_functions
from pathlib import Path as path
import jobs



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
    misc_functions.load_modules(os.path.join(path.home(), ".pyshell", "modules"))
    time.sleep(1)
    clear.clear_shell()
    print(banner)
    # Execute active cronjobs:
    #jobs.__init__(os.path.join(path.home(), ".pyshell", "cronjobs/"))

    # Prompt to insert command      
    preInputString = f"{colors.LIGHTBLUE_EX}\ue62a{colors.RESET} [{colors.GREEN}{os.getlogin()}{colors.RESET}\\/{colors.LIGHTRED_EX}{socket.gethostname()}{colors.RESET}]{colors.LIGHTYELLOW_EX}$->{colors.RESET} "
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
            mc.misc_commands.reload()
        elif cmnd.startswith("cron"):
            cron.cron_cmnd(cmnd)
        elif cmnd.startswith("mkdir"):
            mkdir.makedir(cmnd)
        elif cmnd.startswith("rm"):
            rm.remove(cmnd)
        elif cmnd.startswith("echo"):
            echo.echo(cmnd)
        else:
            print(f"'{cmnd}' does not exists or theres a typo or is not installed as a module.")
            print(f"Check and re-run it!")
            print(f"pypkg <package-name> to install the module!")


if __name__ == "__main__":
    main()