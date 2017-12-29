'''
cd Dropbox/Codes/password_generator
py setup_mac.py
'''

# Dictionary names and keys taken from py2exe settings

dict_console = {
    'author': 'Shun Sakurai',
    'dest_base': 'Password Generator',
    'icon_resources': [(1, './icons/password_icon.icns')],
    'script': 'password_generator.py',
    'version': '1.2.8'
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


if __name__ == "__main__":
    import os
    import shutil
    import subprocess

    folder_dist = 'mac'

    list_excluded = []
    for lib in dict_options['excludes']:
        list_excluded.append('--exclude-module')
        list_excluded.append(lib)

    list_pyinstaller = [
        'python3', '-m',
        'PyInstaller', '--onefile',
        '--distpath', folder_dist,
        '--windowed',
        '--icon', dict_console['icon_resources'][0][1],
        '--name', dict_console['dest_base']
    ] + list_excluded + [dict_console['script']]

    if os.path.exists(folder_dist):
        shutil.rmtree(folder_dist)

    print_with_border('Running PyInstaller')
    subprocess.run(list_pyinstaller)

    print_with_border('Cleaning')
    if os.path.exists('__pycache__'):
        shutil.rmtree('__pycache__')
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists(''.join([dict_console['dest_base'], '.spec'])):
        os.remove(''.join([dict_console['dest_base'], '.spec']))

    print('Executable for v' + dict_console['version'], 'created.')
    subprocess.call(['open', 'mac'])
