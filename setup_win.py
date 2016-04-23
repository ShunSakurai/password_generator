'''
cd Dropbox/Codes/password
py -3.4 setup_win.py py2exe

Libraries used:
import tkinter
from random import sample
from re import search
'''
from distutils.core import setup
import py2exe

setup(
      console=[{'author': 'Shun Sakurai',
                       'dest_base': 'Password Generator',
                       'script': 'password_generator.py',
                       'version': '1.1.4'
                       }],
      options={'py2exe': {
                     'bundle_files': 2,
                     'compressed': True,
                     'excludes': ['_hashlib', '_frozen_importlib', 'argparse', '_lzma', '_bz2', '_ssl', 'calendar', 'datetime', 'difflib', 'doctest', 'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc', 'pyexpat', 'pyreadline', 'zipfile'],
                     }}
      )
