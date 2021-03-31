# What are the things i need to do when i start a project?

# 1. Setup git versioning
# 2. Setup Pipenv
# 3. Create src directory
# 4. Create tests directory
# 5. Pipenv install pytest

from pathlib import Path
import pyinputplus as pyip 

import git
import gittools
import pipenvtools

cwd = Path.cwd()
local = Path(__file__).parent.resolve()

class Project(object):
    def __init__(self):
        self.name = ''
        self.root = ''
        self.src_dir = ''
        self.test_dir = ''
        
        self.author_name = ''
        self.author_email = ''

        self.repo = None
        self.pipenv = None

def new():
    proj = Project()

    cfg = git.GitConfigParser()

    proj.author_name = gittools.get_user_name(cfg)
    proj.author_email = gittools.get_user_email(cfg)

    proj.root = cwd.name
    proj.name = pyip.inputStr(prompt=f"Project name? [default: {cwd.name}", default=cwd.name, blank=True)
    proj.src_dir = Path(pyip.inputFilepath(prompt='Source directory? [default: src/]', default='src/', blank=True))
    proj.test_dir = Path(pyip.inputFilepath(prompt='Test directory? [default: tests/]', default='tests/', blank=True))

    proj.repo = gittools.init_git('.')
    proj.pipenv = pipenvtools.init_pipenv('.')

    return proj
        