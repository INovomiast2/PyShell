def parseFlags(command):
    splitted_cmnd = command.split(' ')
    return splitted_cmnd[1::]


def checkFlags(flags, message):
    if len(flags) <= 0:
        print(message)
        return False
    elif len(flags) >= 1:
        return True