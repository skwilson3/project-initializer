import pytest
from flaky import flaky
import os

from context import src 
from src import utils

def test_working_directory(tmp_path):
    with utils.working_directory(tmp_path):
        assert str(tmp_path) == os.getcwd()

@flaky(max_runs=3)
def test_create_file_relative(tmp_path):
    if not (tmp_path / 'tempfile.txt').exists():
        with utils.working_directory(tmp_path):
            utils.create_file('tempfile.txt')
        assert (tmp_path / 'tempfile.txt').exists()
    else:
        assert False

@flaky(max_runs=3)
def test_create_file_absolute(tmp_path):
    if not (tmp_path / 'tempfile.txt').exists():
        utils.create_file(tmp_path / 'tempfile.txt')
        assert (tmp_path / 'tempfile.txt').exists()
    else:
        assert False

@flaky(max_runs=3)
def test_create_directory_relative(tmp_path):
    if not (tmp_path / 'tempfile').exists():
        with utils.working_directory(tmp_path):
            utils.create_directory('tempfile')
        assert (tmp_path / 'tempfile').exists()
    else:
        assert False

@flaky(max_runs=3)
def test_create_directory_absolute(tmp_path):
    if not (tmp_path / 'tempfile').exists():
        utils.create_directory(tmp_path / 'tempfile')
        assert (tmp_path / 'tempfile').exists()
    else:
        assert False