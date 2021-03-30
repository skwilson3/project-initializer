from context import src 
from src import pipenvtools

from os import path

def test_init(tmpdir):
    """Pipfile should be created successfully"""
    p = tmpdir.mkdir('temp')
    pipenvtools.init(p)
    assert path.join(p,'Pipfile') in p.listdir()