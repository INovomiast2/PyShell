from utils import colors, help
import flags

def echo(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags):
        print(help.message.echo_help)
        return 0
    elif "--help" in command_flags or "-h" in command_flags:
        print(help.message.echo_help)
        return 0
    else:
        if len(command_flags) > 1:
            for i in range(0, len(command_flags)):
                print(str(command_flags[i]).replace('"', ""), end=' ')
            print()
        if len(command_flags) == 1:
            for i in range(0, len(command_flags)):
                print(str(command_flags[i]).replace('"', ""))
                
            if '-e' in command_flags:
                return 0
            elif '-E' in command_flags:
                return 0
            elif '-n' in command_flags:
                return 0
            elif '-v' in command_flags:
                return 0
            elif '-r' in command_flags:
                return 0
            else:
                print()
                return 0

