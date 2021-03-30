import subprocess

def init(dir):
    subprocess.call(['git','init',dir])