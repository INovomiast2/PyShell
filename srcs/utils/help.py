# Help Messages of all the commands

# Path: srcs/utils/help.py

from utils import colors
from utils import dev

class message:
    # cron Command Help Message
    cron_help = f"""
    cron: Is a command that allows you to create, modify, list, delete, activate, and deactivate cron jobs.
    Usage: cron < -n | -m | -l | -d > <name> < --show | --activate | --deactivate >

    | Command      | Description                |
    | {colors.LIGHTBLUE_EX}-n{colors.RESET}           | Create a new cron job      |
    | {colors.LIGHTBLUE_EX}-m{colors.RESET}           | Modify a cron job          |
    | {colors.LIGHTBLUE_EX}-l{colors.RESET}           | List all cron jobs         |
    | {colors.LIGHTBLUE_EX}-d{colors.RESET}           | Delete a cron job          |
    | {colors.LIGHTBLUE_EX}--show{colors.RESET}       | Show a cron job            |
    | {colors.LIGHTBLUE_EX}--activate{colors.RESET}   | Activate a cron job        |
    | {colors.LIGHTBLUE_EX}--deactivate{colors.RESET} | Deactivate a cron job      |
    | {colors.LIGHTBLUE_EX}-h{colors.RESET}           | Show this help message     |

    Examples:
        cron -n test --show | This will create a new cron job with the name 'test' and show the cron job json.
        cron -m test | This will modify the cron job with the name 'test' opening a text editor.
        cron -l | This will list all the cron jobs and show the current status (Active/Inactive).
        cron -d test | This will delete the cron job with the name 'test'.
        cron -d -a/--all | This will delete all the cron jobs.
        cron test --activate | This will activate the cron job with the name 'test'.
        cron test --deactivate | This will deactivate the cron job with the name 'test'.
        cron -h | This will show this help message.

    Note: The cron jobs are stored in the ~/.pyshell/cronjobs directory.
    ** {colors.FONT_EFFECTS.BOLD}Cronjobs by: {dev.get_data('cron')[0]} - {dev.get_data('cron')[1]}{colors.FONT_EFFECTS.RESET_ALL} **
    """
    # cat Command Help Message
    cat_help = f"""
    cat: Is a command that allows you to read the content of a file.
    Usage: cat <file> < --help >

    | Command                                   | Description               |
    | {colors.LIGHTBLUE_EX}<file>{colors.RESET} | The file you want to read |
    | {colors.LIGHTBLUE_EX}--help{colors.RESET} | Show this help message    |

    Examples:
        cat file.txt | This will read the content of the file 'file.txt'.
        cat --help   | This will show this help message.

    ** {colors.FONT_EFFECTS.BOLD}Cat by: {dev.get_data('cat')[0]} - {dev.get_data('cat')[1]}{colors.FONT_EFFECTS.RESET_ALL} **
    """
    # echo Command Help Message
    echo_help = f"""
    echo: Is a command that allows you to print a string to the terminal.
    Usage: echo < -n | -e | -E | -v | -r > <string> | < --help | --version >

    | Command                                       | Description                                |
    | {colors.LIGHTBLUE_EX}-n{colors.RESET}         | Do not print the trailing newline          |
    | {colors.LIGHTBLUE_EX}-e{colors.RESET}         | Enable interpretation of backslash escapes |
    | {colors.LIGHTBLUE_EX}-E{colors.RESET}         | Disable interpretation of backslash escapes|
    | {colors.LIGHTBLUE_EX}-v{colors.RESET}         | Enable interpretation of backslash escapes |
    | {colors.LIGHTBLUE_EX}-r{colors.RESET}         | Enable interpretation of backslash escapes |
    | {colors.LIGHTBLUE_EX}--help{colors.RESET}     | Show this help message                     |
    | {colors.LIGHTBLUE_EX}--version{colors.RESET}  | Show the version of the command            |

    Examples:
        echo "Hello, World!"      | This will print 'Hello, World!' with a trailing newline.
        echo -n "Hello, World!"   | This will print 'Hello, World!' without a trailing newline.
        echo -e "Hello,\\nWorld!"  | This will print 'Hello,' in a line and 'World!' in the next line.
        echo -E "Hello,\\nWorld!"  | This will print 'Hello,\\nWorld!' in the same line.
        echo -v "Hello,\\nWorld!"  | This will print 'Hello,\\nWorld!' in the same line.
        echo -r "Hello,\\nWorld!"  | This will print 'Hello,\\nWorld!' in the same line.
        echo --help               | This will show this help message.
        echo --version            | This will show the version of the command.
    
    ** {colors.FONT_EFFECTS.BOLD}Echo by: {dev.get_data('echo')[0]} - {dev.get_data('echo')[1]}{colors.FONT_EFFECTS.RESET_ALL} **
    """