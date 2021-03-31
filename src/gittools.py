import git
import pyinputplus as pyip 
import configparser
import typing
import pathlib

from . import utils

@utils.path_resolved
def init_git(path: typing.Union[str,pathlib.Path]) -> git.Repo:
    '''
    Initializes a git repository at the specified path

        Parameters:
            path (str | pathlib.Path): The path of the directory where the repository should be initialized
        
        Returns:
            repo (git.Repo): The object-model representation of the newly initialized repository
    '''
    repo = git.Repo.init(path)
    return repo

def get_user_name(cfg: git.GitConfigParser) -> str:
    '''
    Returns the user name specified in the .gitconfig file

        Parameters:
            cfg (git.GitConfigParser): A config parser object pointing at the user's .gitconfig file
        
        Returns:
            name (str): The user's name
    '''
    try:
        return cfg.get_value('user','name')
    except configparser.NoSectionError or configparser.NoOptionError:    
        print('WARNING: Git user name not set.')
        return pyip.inputStr(prompt='Please enter your name: ')

def get_user_email(cfg: git.GitConfigParser) -> str:
    '''
    Returns the user email specified in the .gitconfig file

        Parameters:
            cfg (git.GitConfigparser): A config parser object pointing at the user's .gitconfig file

        Returns:
            email (str): The user's email address
    '''
    try:
        return cfg.get_value('user','email')
    except configparser.NoSectionError or configparser.NoOptionError:
        print('WARNING: Git user email not set.')
        return pyip.inputEmail(prompt='Please enter your email: ')
