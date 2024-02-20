import colorama
import flags

def echo(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags, 'Usage: echo [flags] [string]'):
        return
    else:
        if len(command_flags) > 1:
            for i in range(0, len(command_flags)):
                print(str(command_flags[i]).replace('"', ""), end=' ')
            print()
        if len(command_flags) == 1:
            for i in range(0, len(command_flags)):
                print(str(command_flags[i]).replace('"', ""))
                
            if '-e' in command_flags:
                print()
