import subprocess

from os import path

def init(dir):
    with open(path.join(dir,'Pipfile'), 'w+') as f:
        f.write(r"""
            [[source]]
            url = "https://pypi.org/simple"
            verify_ssl = true
            name = "pypi"

            [packages]

            [dev-packages]
            pytest = "*"
            mockito = "*"

            [requires]
            python_version = "3.9"
            """)