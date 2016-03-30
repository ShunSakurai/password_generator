'''
cd Dropbox/Codes/password/windows
py -3.4 setup_win.py py2exe
'''
from distutils.core import setup
import py2exe

SCRIPT = 'password_generator.py'
VERSION = "1.1.0"
DATA_FILES = []
NAME = "Password Generator"
OPTIONS = {'bundle_files': 2}

setup(
      console=[{'script': SCRIPT, 'version': VERSION, 'dest_base': NAME}],
      options={'py2exe': OPTIONS},
      )
