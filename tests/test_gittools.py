import pytest
import git
import configparser

from context import src
from src import utils
from src import gittools


@pytest.fixture
def cfg():
    cfg = git.GitConfigParser()
    yield cfg
    cfg.release()

@pytest.fixture
def tmpcfg(tmp_path):
    return (tmp_path / 'tmpcfg')

@pytest.fixture
def emptycfg(tmpcfg):
    cfg = git.GitConfigParser(tmpcfg)
    yield cfg
    cfg.release()

def test_git_init(tmpdir):
    gittools.init_git(tmpdir)
    assert len(tmpdir.listdir()) == 1
    assert tmpdir.listdir()[0].basename == '.git'

def test_get_user_name(cfg):
    assert gittools.get_user_name(cfg) == 'Sam Wilson'

def test_get_user_email(cfg):
    assert gittools.get_user_email(cfg) == 'skwilson3@crimson.ua.edu'


def test_get_user_name_notset(emptycfg, capsys, monkeypatch):
    monkeypatch.setattr('pyinputplus.inputStr', lambda prompt: 'Sam Wilson')
    user_name =  gittools.get_user_name(emptycfg)
    assert user_name == 'Sam Wilson'


def test_get_user_email_notset(emptycfg, capsys, monkeypatch):
    monkeypatch.setattr('pyinputplus.inputEmail', lambda prompt: 'skwilson3@crimson.ua.edu')
    user_email = gittools.get_user_email(emptycfg)
    assert user_email == 'skwilson3@crimson.ua.edu'
