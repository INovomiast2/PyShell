import os
import sys
import flags
import socket
import colorama
import execute as ex
import time
import random
import inquirer

def load_modules(directory):
  """Iterates through module files in a directory and displays loading messages."""
  messages = []
  for filename in os.listdir(directory):
    if filename.endswith(".py"):
      module_name = os.path.splitext(filename)[0]
      messages.append(f"Loading module: {module_name} ")
  for msg in messages:
    print("PyShell - " + msg)
    time.sleep(random.random() * 0.2)  # Add random delay for each module
    
def setIcon(file_extension):
    fExtensions = [
        ('.py', ''),
        ('.lnk', ''),
        ('.webp', '󰋩'),
        ('.pdf', ''),
        ('.docx', '󰈙'),
        ('.pptx', '󱎐'),
        ('.xlsx', '󱎏'),
        ('.jpg', '󰋩'),
        ('.png', '󰋩'),
        ('.mp3', '󰎄'),
        ('.wav', '󱑽'),
        ('.java', ''),
        ('.go', ''),
        ('.js', ''),
        ('.json', '󰘦'),
        ('.jsx', ''),
        ('.css', ''),
        ('.html', ''),
        ('.txt', ''),
        ('.md', ''),
        ('.c', ''),
        ('.cpp', ''),
        ('.h', ''),
        ('.hpp', ''),
        ('.exe', '󰏚'),
        ('.dll', '󰏚'),
        ('.msi', '󰏚'),
        ('.bat', '󰏚'),
        ('.sh', ''),
        ('.pyc', ''),
        ('.pyd', ''),
        ('.pyo', ''),
        ('.pyw', ''),
        ('.pyz', ''),
        ('.key', '󰏚'),
    ]
    
    for ext, icon in fExtensions:
        if ext.lower() == file_extension.lower():
            return icon

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
    
    os.system('cls')
    for arg in arguments:
        if arg == "--styled":
            time.sleep(0.5)
            print(banner)
            time.sleep(1)
            print("Starting PyShell 1.0.0...")
            time.sleep(0.5)
            load_modules(os.path.join(os.getcwd(), "../modules"))
            os.system('cls' or 'clear')
            print(banner)
            
            
    preInputString = f"{colorama.Fore.BLUE}\ue62a{colorama.Fore.RESET}[{colorama.Fore.GREEN}{os.getlogin()}{colorama.Fore.RESET}\\/{colorama.Fore.LIGHTRED_EX}{socket.gethostname()}{colorama.Fore.RESET}]{colorama.Fore.LIGHTYELLOW_EX}$->{colorama.Fore.RESET} "
    while True:
        cmnd = input(preInputString)

        if cmnd == "clear":
            os.system('cls')
        elif cmnd == "exit":
            os.system('cls')
            sys.exit(0)
        elif cmnd == "ls":
            directory_content = os.listdir(path=os.getcwd())[::-1]
            for content in directory_content:
                file_name, file_extension = os.path.splitext(os.path.join(os.getcwd() + content))
                if os.path.isdir(f"{os.getcwd()}/{content}"):
                    print(colorama.Fore.BLUE + content + colorama.Fore.RESET)
                else:
                    print(f"{content} {setIcon(file_extension)}")
        elif cmnd == "ls -la":
            os.system('dir')
        elif cmnd.startswith('cd'):
            command_flags = flags.parseFlags(cmnd)
            if flags.checkFlags(command_flags):
                print("Usage: cd <target_directory>")
                continue
            else:
                target_directory = command_flags[0]
                try:
                    os.chdir(target_directory)
                    print(f"You are now on: {os.getcwd()}")
                except FileNotFoundError:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory}´ not found! ")
                except NotADirectoryError:
                    print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory} is not a directory´")
        elif cmnd.startswith('cat'):
            command_flags = flags.parseFlags(cmnd)
            
            if not flags.checkFlags(command_flags, "Usage: cat <file>"):
                continue
            
            if command_flags[1] == "--help":
                print("Usage: cat <file>")
                print("Prints the content of a file.")
                print("Example: cat file.txt")
                continue
               
            try:
                with open(os.path.join(os.getcwd(), command_flags[1]), "r", encoding="utf-8") as file:
                    print(file.read())
            except FileNotFoundError:
                print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{command_flags[1]}` not found!")
            except FileExistsError:
                print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{command_flags[1]}` is a directory!")         
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
            
            if len(command_flags) <= 1:
                print("mkdir <name>")
                continue
            
            if len(command_flags) >= 1:
                try:
                    print(f"Creating {command_flags[1]}...")
                    time.sleep(1)
                    os.mkdir(command_flags[1])
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
