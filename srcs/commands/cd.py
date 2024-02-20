import colorama
import flags
import os


def change_dir(command):
    command_flags = flags.parseFlags(command)
    if not flags.checkFlags(command_flags):
        print("Usage: cd <target_directory>")
    else:
        target_directory = command_flags[0]
        try:
            os.chdir(target_directory)
            print(f"You are now on: {os.getcwd()}")
        except FileNotFoundError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory}´ not found! ")
        except NotADirectoryError:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET}: `{target_directory} is not a directory´")