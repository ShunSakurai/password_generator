"""
This is a setup.py script generated by py2applet
cd Dropbox/Codes/password
py setup_mac.py py2app

Libraries used:
import tkinter
import random
from re import search
"""
from setuptools import setup

setup(
    app=['password_generator.py'],
    name='Password Generator',
    options={'py2app': {
                   'argv_emulation': False,
                   'excludes': ['_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl', 'argparse', 'calendar', 'datetime', 'difflib', 'doctest', 'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc', 'pyexpat', 'pyreadline', 'zipfile'],
                   }},
    setup_requires=['py2app'],
    version='1.2.0',
)
