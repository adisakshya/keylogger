
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'keylogger',
    'author': 'Adisakshya Chauhan',
    'url': 'https://github.com/adisakshya/keylogger',
    'download_url': 'https://github.com/adisakshya/keylogger',
    'author_email': 'adisakshya98@gmail.com',
    'version': '1.0',
    'install_requires': ['pynput'],
    'packages': ['pynput'],
    'scripts': ['bin/keylogger-windows.py'],
    'name': 'keylogger'
    }

setup(**config)
