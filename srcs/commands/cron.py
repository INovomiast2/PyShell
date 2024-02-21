import flags
import os
import sys
import pathlib as path
from utils import colors
from commands import cat
from utils import help, colors

# Set the colorama init
colors.colorama.init()


def cron_cmnd(command):
    command_flags = flags.parseFlags(command)

    # Cronjob Template
    cronjob_template = f"""
    {{
        "job_name": "{command_flags[1]}",
        "interval": {{
            "every": {{
                "months": 0,
                "days": 0,
                "hours": 0,
                "minutes": 0,
                "seconds": 0
            }}
        }},
        "action": "command_to_execute",
        "active": false
        "created_by": "{os.getlogin()}"
    }}
    """

    if not flags.checkFlags(command_flags):
        print(help.message.cron_help)
        return 0
    # Check if first flag is -n, -m, or -l
    if command_flags[0] == '-n':
        # Check if a name was given
        if command_flags[1::] == '' or command_flags[1] == None:
            print("cron: No name given")
            return 0
        else:
            # This will create a new cron job
            if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
                # Now we check if the cronjob json exists or not
                if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json'):
                    print(f"cron: '{command_flags[1]}' - Cron job already exists")
                    return 0
                else:
                    # We create the cronjob json file
                    with open(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json', 'w') as f:
                        f.write(cronjob_template)
                        print(f"cron: '{command_flags[1]}' - Cron job created")
                    f.close()
            else:
                os.mkdir(f"{path.Path.home()}/cronjobs")
                print("cron: cronjobs created")
                cron_cmnd(command)
    elif command_flags[0] == '-m':
        # This will modify an existing cron job
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json'):
                # If this cronjob exists we will open a editor to modify the cronjob
                os.system(f"nano {path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json")
                # Just for a fast check, we will get the mtime of the file.
                mtime = os.path.getmtime(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json")
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
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
            cronjobs = os.listdir(f"{path.Path.home()}/.pyshell/cronjobs")
            if len(cronjobs) > 0:
                for cronjob in cronjobs:
                    print(f"{cronjob.replace('.json', '')} | {colors.LIGHTGREEN_EX}Active{colors.RESET}" if '"active": true' in open(f"{path.Path.home()}/.pyshell/cronjobs/{cronjob}").read() else f"{cronjob.replace('.json', '')} | {colors.LIGHTRED_EX}Inactive{colors.RESET}")
            else:
                print("cron: No cronjobs found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif command_flags[0] == "-s":
        print(command_flags[1])
        # This will show the cronjob
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs/"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json'):
                os.system(f"cat {path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json")
                return 0
            else:
                print(f"cron: '{command_flags[1]}' - Cronjob not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif command_flags[0] == '-d':
        # This will delete the cronjob
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json'):
                os.remove(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[1]}.json")
                print(f"cron: '{command_flags[1]}' - Cron job deleted")
                return 0
            elif command_flags[1] == '-a' or command_flags[1] == '--all':
                cronjobs = os.listdir(f"{path.Path.home()}/.pyshell/cronjobs")
                if len(cronjobs) > 0:
                    for cronjob in cronjobs:
                        os.remove(f"{path.Path.home()}/.pyshell/cronjobs/{cronjob}")
                    print("cron: All cronjobs deleted")
                    return 0
                else:
                    print("cron: No cronjobs found")
                    return 0
            else:
                print(f"cron: '{command_flags[1]}' - Cron job not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif "--activate" in command_flags:
        # This will activate the cronjob
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json'):
                with open(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json", 'r') as f:
                    cronjob = f.read()
                    f.close()
                cronjob = cronjob.replace('"active": false', '"active": true')
                with open(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json", 'w') as f:
                    f.write(cronjob)
                    f.close()
                print(f"cron: '{command_flags[0]}' - Cron job activated")
                return 0
            else:
                print(f"cron: '{command_flags[0]}' - Cron job not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif "--deactivate" in command_flags:
        # This will deactivate the cronjob
        if os.path.exists(f"{path.Path.home()}/.pyshell/cronjobs"):
            # Now we check if the cronjob json exists or not
            if os.path.exists(f'{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json'):
                with open(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json", 'r') as f:
                    cronjob = f.read()
                    f.close()
                cronjob = cronjob.replace('"active": true', '"active": false')
                with open(f"{path.Path.home()}/.pyshell/cronjobs/{command_flags[0]}.json", 'w') as f:
                    f.write(cronjob)
                    f.close()
                print(f"cron: '{command_flags[0]}' - Cron job deactivated")
                return 0
            else:
                print(f"cron: '{command_flags[0]}' - Cron job not found")
                return 0
        else:
            print("cron: cronjobs not found")
            return 0
    elif command_flags[0] == '-h' or command_flags[0] == '--help':
        print(help.message.cron_help)
        return 0
    else:
        print(f"cron: '{command_flags[0]}' - Invalid flag")
        return 0