import functools
import pathlib
import typing
import contextlib

import os

ValidPath = typing.Union[str, pathlib.Path]

def path_resolved(func: callable) -> callable:
    '''
    Enables functions to use both absoulte and relative paths
    '''
    @functools.wraps(func)
    def wrapper(path: ValidPath, strict = False):
        return func(pathlib.Path(path).resolve(strict=strict))
    return wrapper

@path_resolved
def create_file(path: ValidPath):
    '''
    Creates a file specified by path

        Parameters:
            path (str | pathlib.Path): The path of the file to be created
    '''
    path.touch()

@path_resolved
def create_directory(path: ValidPath):
    '''
    Creates a directory specified by path

        Parameters:
            path (str | pathlib.Path): The path of the directory to be created
    '''
    path.mkdir()

@path_resolved
@contextlib.contextmanager
def working_directory(path):
    prev_cwd = pathlib.Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)
        return