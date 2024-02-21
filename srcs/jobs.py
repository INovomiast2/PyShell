# Cronjobs execution.
"""
    This file it's going to be used to parse and execute the cronjobs.
    NOTE: Cronjobs are stored at: ~/.pyshell/cronjobs

    Basic explanation of the functionality:
        - Read the cronjobs file.
        - Parse the cronjobs.
        - Execute the cronjobs.
        - Log the output of the cronjobs.
        - Send the output to the user.
"""

import os
import time
import datetime
import subprocess
import re
import sys
import json
from pathlib import Path as path

# Cronjob Validator:
def validator(directory):
    # List all the files in the cronjobs directory:
    files = os.listdir(os.path.join(path.home(), '.pyshell', 'cronjobs'))
    print(files)
    # Check if the file exists:
    for file in files:
        if len(files) == 0:
            return 0
        else:
            # JSON parse the file:
            with open(os.path.join(path.home(), '.pyshell', 'cronjobs') + '/' + file, 'r') as f:
                data = json.load(f)
            # Validate the JSON job file (every file is a job):
            if not "job_name" in data:
                raise ValueError("job_name is not defined.")
            if not "interval" in data or data["interval"] == "":
                raise ValueError("interval is not defined.")
            if not "action" in data or data["action"] == "":
                raise ValueError("command is not defined.")
            if data["created_by"] != os.getenv('USER'):
                raise ValueError("You are not the owner of this job. (Only the owner can execute the job).")
            else:
                return data
        
def log_output(job, output):
    # Log the output of the command:
    with open(f'/home/{os.getenv("USER")}/.pyshell/logs/{job["job_name"]}.log', 'a') as f:
        f.write(f'[{datetime.datetime.now()}] - {output}\n')
    f.close()

def log_error(job, error):
    # Log the error of the command:
    with open(f'/home/{os.getenv("USER")}/.pyshell/logs/{job["job_name"]}.log', 'a') as f:
        f.write(f'[{datetime.datetime.now()}] - {error}\n')
    f.close()

def send_output(output):
    # Send the error on screen
    print(f'[{datetime.datetime.now()}] - {output}')
    return

def send_error(error):
    # Send the error on screen
    print(f'[{datetime.datetime.now()}] - {error}')
    return

def execute_job(job):
    # Check if job is active:
    if not job["interval"]["every"]["active"] == "true":
        return
    else:
        # Check for the interval:
        if job["interval"]["every"]["months"] > 0:
            time.sleep(job["interval"]["every"]["months"] * 2592000)
        elif job["interval"]["every"]["days"] > 0:
            time.sleep(job["interval"]["every"]["days"] * 86400)
        elif job["interval"]["every"]["hours"] > 0:
            time.sleep(job["interval"]["every"]["hours"] * 3600)
        elif job["interval"]["every"]["minutes"] > 0:
            time.sleep(job["interval"]["every"]["minutes"] * 60)
        elif job["interval"]["every"]["seconds"] > 0:
            time.sleep(job["interval"]["every"]["seconds"])
        else:
            return
        # Execute the command:
        try:
            output = subprocess.check_output(job["action"], shell=True)
            log_output(job, output)
            send_output(output)
        except subprocess.CalledProcessError as e:
            log_error(job, e)
            send_error(e)

def __init__(cronjob):
    # Validate the cronjob:
    job = validator(cronjob)
    # Execute the cronjob:
    execute_job(job)