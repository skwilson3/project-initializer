from context import src
from src import gittools

from os import path

def test_init(tmpdir):
    d = tmpdir.mkdir('temp')
    gittools.init(d)
    assert len(d.listdir()) == 1
    assert path.split(d.listdir()[0])[-1] == '.git'