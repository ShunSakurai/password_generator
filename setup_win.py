'''
cd Dropbox/Codes/password_generator
py -3.4 setup_win.py py2exe

Libraries used:
import tkinter
import random
from re import search
'''
import os
import shutil

if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('windows'):
    shutil.rmtree('windows')

from distutils.core import setup
import py2exe

setup(
    console=[{
        'author': 'Shun Sakurai',
        'dest_base': 'Password Generator',
        'script': 'password_generator.py',
        'version': '1.2.1'
    }],
    options={'py2exe': {
        'bundle_files': 2,
        'compressed': True,
        'excludes':['_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl', 'argparse', 'calendar', 'datetime', 'difflib', 'doctest', 'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc', 'pyexpat', 'pyreadline', 'zipfile'],
    }}
)

os.rename('dist', 'windows')
if os.path.exists('__pycache__'):
    shutil.rmtree('__pycache__')
