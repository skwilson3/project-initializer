import subprocess

from . import utils

class Pipenv(object):
    def __init__(self):
        subprocess.call(['pipenv','shell'])

    def deactivate(self):
        subprocess.call(['deactivate'])

    def _execute(self, command):
        subprocess.call(['pipenv', command])

    def lock(self):
        self._execute('lock')

    def install(self, package, dev=False):
        cmd = f'install {package}'
        if dev:
            cmd += ' --dev'
        self._execute(f'install {package}')

    def uninstall(self, package):
        self._execute(f'uninstall {pacakge}')

def init_pipenv(path):
    with utils.working_directory(path):
        return Pipenv()
    