import os
import subprocess
import shutil

def mkdir(path):
    """Creates a directory at the given path"""
    os.makedirs(path, exist_ok=True)

def touch(path):
    """Creates an empty file at the given path"""
    with open(path, 'a'):
        os.utime(path, None)


def rimraf(path):
    """Deletes an entire directory recursively at the given path"""
    shutil.rmtree(path)


def run(command: str) -> tuple[int, str, str]:
    """Runs a command as a subprocess and return the exit code, stdout and stderr

    WARNNING: You can run anything here, be careful with the input!
        
    Args:
        command (str): The command to run, e.g. "python3 -m pytest two-sum/tests.py"

    Returns:
        (int, str, str): A tuple containing the exit code, stdout and stderr
    """

    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr
