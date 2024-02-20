import os
import sys
import flags
import socket
import colorama
import execute as ex
import time
import random
import inquirer
from commands import clear
from commands import exit
from commands import ls
from commands import cd
from commands import cat

def load_modules(directory):
    messages = []

    if len(os.listdir(directory)) <= 0:
        print("PyShell - No modules where found")
        pass

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            module_name = os.path.splitext(filename)[0]
            messages.append(f"Loading module: {module_name} ")
        for msg in messages:
            print("PyShell - " + msg)
            time.sleep(random.random() * 0.2)  # Add random delay for each module

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
    load_modules(os.path.join(os.getcwd(), "../modules"))
    time.sleep(1)
    clear.clear_shell()
    print(banner)

    # Prompt to insert command      
    preInputString = f"{colorama.Fore.BLUE}\ue62a{colorama.Fore.RESET}[{colorama.Fore.GREEN}{os.getlogin()}{colorama.Fore.RESET}\\/{colorama.Fore.LIGHTRED_EX}{socket.gethostname()}{colorama.Fore.RESET}]{colorama.Fore.LIGHTYELLOW_EX}$->{colorama.Fore.RESET} "
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
            questions = [
                inquirer.Text("username", "Insert your Username"),
                inquirer.Password("usrpwd", '*')
            ]
            answers = inquirer.prompt(questions)
        elif cmnd == "reload":
            print("Reloading Terminal...")
            time.sleep(0.5)
            sys.exit(1)
        elif cmnd.startswith("cron"):
            command_flags = flags.parseFlags(cmnd)
            
            if len(command_flags) <= 1:
                print("cron < -n | -m | -l > <name> < -e | --show >")
                continue
        elif cmnd.startswith("mkdir"):
            command_flags = flags.parseFlags(cmnd)
            
            if not flags.checkFlags(command_flags):
                print("mkdir <name>")
                continue
            
            if flags.checkFlags(command_flags):
                try:
                    print(f"Creating {command_flags[0]}...")
                    time.sleep(1)
                    os.mkdir(command_flags[0])
                except FileExistsError:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {command_flags[1]} already exists!")
        elif cmnd.startswith("rm"):
            cmd_flags = flags.parseFlags(cmnd)
            
            if flags.checkFlags(cmd_flags, "rm <file>") == False:
                continue
            
            if flags.checkFlags(cmd_flags, "") == True:
                try:
                    os.remove(os.path.join(os.getcwd(), cmd_flags[0]))
                    print(f"{cmd_flags[0]}: removed successfully!")
                except FileNotFoundError:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {cmd_flags[1]} not found!")
                except PermissionError as e:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: {e}!")
                    
        else:
            print(f"'{cmnd}' does not exists or theres a typo or is not installed as a module.")
            print(f"Check and re-run it!")
            print(f"pypkg <package-name> to install the module!")
            


if __name__ == "__main__":
    print("Hola Mundo!!")
    main()
