import subprocess

from . import utils

class Pipenv(object):
    '''
    A calss to represent a Pipenv environment for a project

    ...
    Methods
    -------
    deaectivate(command):
        Deactivates the environment

    lock():
        Locks the Pipfile

    install(package, dev-False):
        Installs a package

    uninstall(package):
        Uninstalls a package
    '''
    def __init__(self):
        '''
        Creates the pipenv by running shell command `pipenv shell` and 
        instantiates Pipenv object
        '''
        subprocess.call(['pipenv','shell'])

    def deactivate(self):
        '''Deactivates pipenv'''
        subprocess.call(['deactivate'])

    def _execute(self, command):
        '''
        Executes the given command

            Parameters:
                command (str): The command to be executed
        '''
        subprocess.call(['pipenv', command])

    def lock(self):
        '''Locks the Pipfile'''
        self._execute('lock')

    def install(self, package, dev=False):
        '''
        Installs a package as a dependency

            Parameters:
                package (str): The name of the package to be installed
                dev (bool): True to install the package as a dev dependency, False otherwise (default)
        '''
        cmd = f'install {package}'
        if dev:
            cmd += ' --dev'
        self._execute(f'install {package}')

    def uninstall(self, package):
        '''
        Uninstalls a package

            Parameters:
                package (str): The name of the package to be uninstalled
        '''
        self._execute(f'uninstall {pacakge}')

def init_pipenv(path):
    '''
    Initializes the Pipenv at the given path

        Parameters:
            path (str | pathlib.Path): The path to initialize the pipenv at
        
        Returns:
            pipenv (Pipenv): The corresponding Pipenv object
    '''
    with utils.working_directory(path):
        return Pipenv()
    