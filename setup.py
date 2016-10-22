from setuptools import setup, find_packages

setup(
    name = 'reqcheck',
    version = '0.1.1',
    packages = find_packages(),
    install_requires = [
        'requests',
        'six',
        'tabulate',
    ],
    author = 'Jozef Leskovec',
    author_email = 'jozefleskovec@gmail.com',
    description = 'Compare installed Python package versions with PyPI',
    license = 'MIT',
    keywords = 'requirements check compare installed virtualenv venv pypi package packages version versions',
    url = 'https://github.com/jaleskovec/reqcheck',
    entry_points = {
        'console_scripts': [
            'reqcheck = reqcheck:cmdline',
        ],
    },
)
