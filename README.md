# password_generator
Simple password generators

[Japanese README](https://github.com/ShunSakurai/password_generator/blob/master/README_jpn.md) is also available.

![UI](https://raw.github.com/wiki/ShunSakurai/password_generator/password_ui.png)

## Description
The purpose of developing this tool is to create a **simple** password generator that lets the user copy the generated password to the clipboard with a single click.
Many programs and websites out there require three actions (drag on the password, right-click, and copy) to do this.

This program is coded in Python with tkinter and is distributed in .exe format through [py2exe](http://www.py2exe.org/), and in Mac .app format through [py2app](https://pythonhosted.org/py2app/).

## Installation
It is currently available for Windows and Mac at [Releases](https://github.com/ShunSakurai/password_generator/releases). An iOS version is also available as a [Pythonista](http://omz-software.com/pythonista/) code. You can run it by using the URL scheme pythonista://password_iphone.py or add it to the home screen using [Pythonista Shortcut](http://omz-software.com/pythonista/shortcut/). Update: the server doesn't seem to be working lately. Please see the instruction in the **iOS** section below.

If you have the Python environment installed, you can run the source code with `python(3) password_generator.py` or `import password_generator` on any OS.

### Windows
All you have to do for installation and upgrading is to download and run the installer.

This program needs to be **kept in the folder** to work. It does not work by itself.

### Mac
- Download Password.Generator.app.zip and decompress it
- Move the .app file to the "Applications" folder. You can remove the enclosing folder

If it does not run itself, please do the following:

- Place the .app file somewhere you like. You can remove the enclosing folder
- Right-click Password Generator.app, click "Show Package Contents" and create an alias of Password Generator.app/Contents/MacOS/Password Generator
- Move the alias to the "Applications" folder

### iOS
- Purchase Pythonista first
- Somehow copy and paste the code into your app
- I designed the code to fit my iPhone 5/SE screen. I tried my best to make it as proportional as possible, but please modify the parameters to fit your size
- Change the length and the number of the passwords manually

## Build

### Windows
To convert the Python code to an .exe file, and to create an installer, follow steps below.

Requirements and procedures for the .exe file:

- Python 3.4 (py2exe is not compatible with Python 3.5 as far as I know)
- [py2exe](http://www.py2exe.org/)
- Run `py -3.4 setup.py py2exe` on a Windows machine

Requirements and procedures for the installer:

- [Inno Setup](http://www.jrsoftware.org/isdl.php)
- Open setup_installer.iss with Inno Setup Compiler and click Build > Compile

### Mac
To convert the Python code to an .app file, follow steps below.

Requirements and procedures for the .app file:

- Python 3.4 or later
- [py2exe](http://www.py2exe.org/)
- Run `py setup_mac.py py2app` on a Mac

## Usage
You can open the program by double-clicking Password Generator.exe / Password Generator or its alias.

In the right pane, click one of the choices. It is now copied to your clipboard!
Use the left pane to modify settings. You can switch symbols / alphabetical characters / numerical characters on and off. The length of a password and the number of choices generated can be set to any figure from 1 to 20.

![Selected](https://raw.github.com/wiki/ShunSakurai/password_generator/password_selected.png)

The tool only generates passwords and allows you to copy one to the clipboard.
No storing feature is provided or planned to be.

## Features to come
### Working on
- Make the code more [readable](http://www.amazon.com/dp/0596802293)
- Add an ability to store the settings
- Prepare the icon

### Maybe later
- Add an ability to edit characters used
- Add keyboard shortcuts (e.g. 1 to 10)
- (iOS) Add UI elements to set the length and the number of the passwords

Please [let me know](https://app.asana.com/-/share?s=132674863519248-e1JyDAuWLW0WnFErIjTrbz57EAmE077JUvQ45Y5pF43-29199191293549) if you need any of the features as soon as possible.

## History
"*" at the beginning means bug-fixing.
For detailed history, please go to [Releases](https://github.com/ShunSakurai/password_generator/releases).

### Newest version
- Semiautomate the set-up process with shutil module

### v1.2.1, July 4, 2016
- Create the installer
- Update information about the iOS version
- Add contact information

### v1.2.0, April 23, 2016
- Reseed when refreshing
- Reduce the size of the dist folder and the .app file

### v1.1.3, April 13, 2016
- * Correct indent so that password is copied every time when necessary

### v1.1.2, April 8, 2016
- Reduce the button border width for the Windows version
- * Resolve an issue where button is not re-enabled on Windows

### v1.1.0, March 31, 2016
- Distribute the binaries
- Create README_jpn.md

### v1.0.0, March 28, 2016
- Add to GitHub
- Create README.md

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any [feedback](https://app.asana.com/-/share?s=132674863519248-e1JyDAuWLW0WnFErIjTrbz57EAmE077JUvQ45Y5pF43-29199191293549) and contribution is welcome!

## License
You can use it for free. Personal use only. I do not take any responsibility for any damage caused by using this program.

Please note that it is stated that the pseudo-random generators of Python's random module should not be used for security purposes.
https://docs.python.org/3/library/random.html#module-random

© 2016 Shun Sakurai

## Basic idea
- Prepare a string containing the following characters
- Choose characters randomly from the string below
- If "num" checkbutton is on, and the "length" is 2 and over, the password contains at least one numerical character
- **No character is duplicated in one password**, unless the password is longer than the length of the string. This can be less secure, but I prefer the passwords look this way

> string = [chr(c) for c in range(33, 127)]
>
> Symbols:
> 33 !, 34 ", 35 #, 36 $, 37 %, 38 &, 39 ', 40 (, 41 ), 42 *, 43 +, 44 ,, 45 -, 46 ., 47 /,
> 58 :, 59 ;, 60 <, 61 =, 62 >, 63 ?, 64 @,
> 123 {, 124 |, 125 }, 126~
>
> Alphabets:
> 65 A, 66 B, 67 C, 68 D, 69 E, 70 F, 71 G, 72 H, 73 I, 74 J, 75 K, 76 L, 77 M, 78 N, 79 O, 80 P, 81 Q, 82 R, 83 S, 84 T, 85 U, 86 V, 87 W, 88 X, 89 Y, 90 Z,
> 91 [, 92 \, 93 ], 94 ^, 95 _, 96 `, 97 a, 98 b, 99 c, 100 d, 101 e, 102 f, 103 g, 104 h, 105 i, 106 j, 107 k, 108 l, 109 m, 110 n, 111 o, 112 p, 113 q, 114 r, 115 s, 116 t, 117 u, 118 v, 119 w, 120 x, 121 y, 122 z,
>
> Numbers:
> 48 0, 49 1, 50 2, 51 3, 52 4, 53 5, 54 6, 55 7, 56 8, 57 9,

