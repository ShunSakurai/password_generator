"""
This is a setup.py script generated by py2applet
cd Dropbox/Codes/password_generator
py setup_mac.py py2app

Libraries used:
import tkinter
import random
from re import search
"""
import os
import shutil

if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('mac'):
    shutil.rmtree('mac')

from setuptools import setup

version = '1.2.2'

setup(
    app=['password_generator.py'],
    name='Password Generator',
    options={
        'py2app': {
            'argv_emulation': False,
            'excludes': [
                '_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl',
                'argparse', 'calendar', 'datetime', 'difflib', 'doctest',
                'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc',
                'pyexpat', 'pyreadline', 'zipfile'
            ],
            'iconfile': 'icons/password_icon.icns'
        }
    },
    setup_requires=['py2app'],
    version=version,
)

os.rename('dist', 'mac')
if os.path.exists('__pycache__'):
    shutil.rmtree('__pycache__')

print('.app file v' + version, 'created.')
