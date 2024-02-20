import flags
import os
import sys

def cron_cmnd(command):
    command_flags = flags.parseFlags(command)
    
    if not flags.checkFlags(command_flags):
        print("cron < -n | -m | -l > <name> < -e | --show >")
        pass