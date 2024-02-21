# Dev data stored here.

# Path: srcs/utils/dev.py

def get_data(command):
    # This function returns the author and version of the command.
    commands_data = {
        "cat": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "cron": {
            "author": "INovomiast2",
            "version": "1.0.5"
        },
        "echo": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "exit": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "help": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "ls": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "pwd": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "rm": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "touch": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "clear": {
            "author": "INovomiast2",
            "version": "1.0.0"
        },
        "cron": {
            "author": "INovomiast2",
            "version": "1.0.5"
        }
    }
    return commands_data[command]["author"], commands_data[command]["version"]