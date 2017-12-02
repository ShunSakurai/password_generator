'''
cd Dropbox/Codes/password_generator
py setup_mac.py
'''

# Installing PyInstaller that supports Python 3.6
'''
git clone https://github.com/pyinstaller/pyinstaller.git
cd pyinstaller
py setup.py install
'''
# Dictionary names and keys taken from py2exe settings

dict_console = {
    'author': 'Shun Sakurai',
    'dest_base': 'Password Generator',
    'icon_resources': [(1, './icons/password_icon.icns')],
    'script': 'password_generator.py',
    'version': '1.2.6'
}
dict_options = {
    'excludes': [
        '_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl',
        'argparse', 'calendar', 'datetime', 'difflib', 'doctest',
        'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc',
        'pyexpat', 'pyreadline', 'zipfile'],
}


def print_with_border(message):
    border = '='
    length = 20
    print(border * length, message, border * length)


def zero_pad(str_ver):
    list_ver = str_ver.split('.')
    str_ver2 = str_ver + '.0' * (4 - len(list_ver))
    return str_ver2


folder_dist = 'mac'

list_excluded = []
for lib in dict_options['excludes']:
    list_excluded.append('--exclude-module')
    list_excluded.append(lib)

list_pyinstaller = [
    'pyinstaller', '--onefile',
    '--distpath', folder_dist,
    '--windowed',
    '--icon', dict_console['icon_resources'][0][1],
    '--name', dict_console['dest_base']
] + list_excluded + [dict_console['script']]

if __name__ == "__main__":
    import os
    import shutil
    import subprocess

    if os.path.exists(folder_dist):
        shutil.rmtree(folder_dist)

    print_with_border('Running PyInstaller')
    subprocess.run(list_pyinstaller)

    print_with_border('Cleaning')
    shutil.rmtree('__pycache__')
    shutil.rmtree('build')
    os.remove(''.join([dict_console['dest_base'], '.spec']))

    print('Executable and installer for v' + dict_console['version'], 'created.')
