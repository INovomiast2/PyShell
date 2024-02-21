import flags
import os
import sys
import pathlib as path
import colorama
from utils import colors
from commands import cat

# Cronjob Template
cronjob_template = f"""
{{
    "job_name": "test",
    "interval": {{
        "every": {{
            "months": 0,
            "days": 0,
            "hours": 0,
            "active": false
        }}
    }},
    "action": "command_to_execute",
    "created_by": "{os.getlogin()}"
}}
"""


def cron_cmnd(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags):
        print(f"{colors.LIGHTGREEN_EX}cron{colors.RESET} < {colors.LIGHTBLUE_EX}-n{colors.RESET} | {colors.LIGHTBLUE_EX}-m{colors.RESET} | {colors.LIGHTBLUE_EX}-l{colors.RESET} | {colors.LIGHTBLUE_EX}-d{colors.RESET} | {colors.LIGHTBLUE_EX}--activate{colors.RESET} > <name> < -e | --show >")
        return 0

    # Check if first flag is -n, -m or -l
    if command_flags[0] == '-n':
        # Check if a name was given
        if command_flags[1::] == '' or command_flags[1] == None:
            print("cron: No name given")
            return 0
        else:
            # This will create a new cron job
            if os.path.exists(f"{path.Path.home()}/cronjobs"):
                # Now we check if the cronjob json exists or not
                if os.path.exists(f'{path.Path.home()}/cronjobs/{command_flags[1]}.json'):
                    print(f"cron: '{command_flags[1]}' - Cron job already exists")
                    return 0
                else:
                    # We create the cronjob json file
                    with open(f'{path.Path.home()}/cronjobs/{command_flags[1]}.json', 'w') as f:
                        f.write(cronjob_template)
                        print(f"cron: '{command_flags[1]}' - Cron job created")
                    f.close()
            else:
                os.mkdir(f"{path.Path.home()}/cronjobs")
                print("cron: cronjobs created")
                cron_cmnd(command)
    elif command_flags[0] == '-m':
        # This will modify an existing cron job
        if os.path.exists(f"{path.Path.home()}/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/cronjobs/{command_flags[1]}.json'):
                # If this cronjob exists we will open a editor to modify the cronjob
                os.system(f"nano {path.Path.home()}/cronjobs/{command_flags[1]}.json")
                # Just for a fast check, we will get the mtime of the file.
                mtime = os.path.getmtime(f"{path.Path.home()}/cronjobs/{command_flags[1]}.json")
                if mtime > 0:
                    print(f"cron: '{command_flags[1]}' - Cron job modified")
                    return 0
                else:
                    print(f"cron: '{command_flags[1]}' - Cron job not modified")
                    return 0
            else:
                print(f"cron: '{command_flags[1]}' - Cron job not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif command_flags[0] == '-l':
        # This will list all the cronjobs avaliable and if their active or not
        if os.path.exists(f"{path.Path.home()}/cronjobs"):
            cronjobs = os.listdir(f"{path.Path.home()}/cronjobs")
            if len(cronjobs) > 0:
                for cronjob in cronjobs:
                    print(f"{cronjob.replace('.json', '')} | {colorama.Fore.LIGHTGREEN_EX}Active{colorama.Fore.RESET}" if '"active": true' in open(f"{path.Path.home()}/cronjobs/{cronjob}").read() else f"{cronjob.replace('.json', '')} | {colorama.Fore.LIGHTRED_EX}Inactive{colorama.Fore.RESET}")
            else:
                print("cron: No cronjobs found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif command_flags[1] == '-e' or command_flags[1] == '--show':
        # This will show the cronjob
        if os.path.exists(f"{path.Path.home()}/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/cronjobs/{command_flags[0]}.json'):
                os.system(f"cat {path.Path.home()}/cronjobs/{command_flags[0]}.json")
                return 0
            else:
                print(f"cron: '{command_flags[1]}' - Cronjob not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0 
    else:
        print(f"cron: '{command_flags[0]}' - Invalid flag")
        return 0