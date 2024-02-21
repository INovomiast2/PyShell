import colorama
import flags
import os


def change_dir(command):
    command_flags = flags.parseFlags(command)
    if not flags.checkFlags(command_flags):
        os.chdir(os.path.expanduser("~"))
        print(f"You are now on: {os.getcwd()}")
        return 0
    else:
        if (command_flags[0] == "-h") or (command_flags[0] == "--help"):
            print("Usage: cd <target_directory>")
            return 0

        target_directory = command_flags[0]
        try:
            os.chdir(target_directory)
            print(f"You are now on: {os.getcwd()}")
            return 0
        except FileNotFoundError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory}´ not found! ")
            return 1
        except NotADirectoryError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory} is not a directory´")
            return 1