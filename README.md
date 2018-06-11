# Password Generator
Simple password generators

[Japanese README](https://github.com/ShunSakurai/password_generator/blob/master/README_jpn.md) is also available.

![UI](https://raw.github.com/wiki/ShunSakurai/password_generator/password_ui.png)

## Description
The purpose of developing this tool is to create a **simple** password generator that lets the user copy the generated password to the clipboard with a single click.
Many programs and websites out there require three actions (drag on the password, right-click, and copy) to do this.

This program is coded in Python with tkinter and is distributed in .exe format through [PyInstaller](http://www.pyinstaller.org/) and [Verpatch](https://ddverpatch.codeplex.com/releases), and in Mac .app format through [PyInstaller](http://www.pyinstaller.org/).

## Installation
The installer and executable are available for Windows and Mac at [Releases](https://github.com/ShunSakurai/password_generator/releases). An iOS version is also available as a [Pythonista](http://omz-software.com/pythonista/) code. You can run it by using the URL scheme pythonista://password_iphone.py or add it to the home screen.

If you have the Python environment installed, you can run the source code with `python(3) password_generator.py` or `import password_generator` on any OS.

### Windows
All you have to do for installation and upgrading is to download and run the installer.

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

You can create a home screen shortcut in Pythonista by choosing [Wrench] icon > [Home Screen], or in Safari opening the following link, tapping [Share] icon, and choosing [Add to Home Screen].
```
data:text/html;charset=UTF-8,<title>Password</title><meta name="apple-mobile-web-app-capable" content="yes"><link rel="apple-touch-icon" href="https://raw.github.com/wiki/ShunSakurai/password_generator/home_icon.png"><script>navigator.standalone?location="pythonista://password_iphone.py":alert("Add to home screen.")</script>
```

## Build

### Requirements
- [Python 3](https://www.python.org/downloads/)
- [PyInstaller](http://www.pyinstaller.org/)
- [Verpatch](https://ddverpatch.codeplex.com/releases), add it to PATH (required for Windows)
- [Inno Setup](http://www.jrsoftware.org/isdl.php) (required for Windows)

### Windows
To convert the Python code to an .exe file and to create an installer, follow the steps below.

- Run `py -B setup_win.py` on a Windows machine. `-B` is optional
- You may have to set alias to make py = python3

### Mac
To convert the Python code to an .app file, follow steps below.

- Run `py -B setup_mac.py` on a Mac. `-B` is optional
- You may have to set alias to make py = python3

## Usage
You can open the program by double-clicking Password Generator.exe / Password Generator or its alias.

In the right pane, click one of the choices. It is now copied to your clipboard!
Use the left pane to modify settings. You can switch symbols / alphabetical characters / numerical characters on and off. The length of a password and the number of choices generated can be set to any figure from 1 to 20.

![Selected](https://raw.github.com/wiki/ShunSakurai/password_generator/password_selected.png)

The tool only generates passwords and allows you to copy one to the clipboard. No storing feature is provided or planned to be.

## Features to come
### Working on
- Make the code more [readable](http://www.amazon.com/dp/0596802293)
- Add an ability to store settings

### Maybe later
- Add keyboard shortcuts (e.g. 1 to 10)

Please let me know from [Github Issues](https://github.com/ShunSakurai/password_generator/issues) or [Asana](https://app.asana.com/0/264055467962183/list) if you need any of the features as soon as possible.

## History
For detailed history, please go to [Releases](https://github.com/ShunSakurai/password_generator/releases).

"*" at the beginning means bug-fixing.

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any feedback and contribution from [Github Issues](https://github.com/ShunSakurai/password_generator/issues) or [Asana](https://app.asana.com/0/264055467962183/list) is welcome!

## License
You can use it for free. Personal use only. I do not take any responsibility for any damage caused by using this program.

Please note that it is stated that the pseudo-random generators of Python's random module should not be used for security purposes.
https://docs.python.org/3/library/random.html#module-random

© 2016-2018 Shun Sakurai

## Basic idea
- This program uses four groups of strings, with the default being as shown below
- Choose a character randomly from each group of strings
- Choose the rest of characters to fill the length of the passwords
- **No character is duplicated in one password**, unless the password is longer than the total length of the string. This can be less secure, but I prefer the passwords look this way

> string = [chr(c) for c in range(33, 127)]
>
> Symbols:
> 33 !, 34 ", 35 #, 36 $, 37 %, 38 &, 39 ', 40 (, 41 ), 42 *, 43 +, 44 ,, 45 -, 46 ., 47 /,
> 58 :, 59 ;, 60 <, 61 =, 62 >, 63 ?, 64 @,
> 123 {, 124 |, 125 }, 126~
>
> Capital letters:
> 65 A, 66 B, 67 C, 68 D, 69 E, 70 F, 71 G, 72 H, 73 I, 74 J, 75 K, 76 L, 77 M, 78 N, 79 O, 80 P, 81 Q, 82 R, 83 S, 84 T, 85 U, 86 V, 87 W, 88 X, 89 Y, 90 Z,
>
> Lowercase letters:
> 91 [, 92 \, 93 ], 94 ^, 95 _, 96 `, 97 a, 98 b, 99 c, 100 d, 101 e, 102 f, 103 g, 104 h, 105 i, 106 j, 107 k, 108 l, 109 m, 110 n, 111 o, 112 p, 113 q, 114 r, 115 s, 116 t, 117 u, 118 v, 119 w, 120 x, 121 y, 122 z,
>
> Numbers:
> 48 0, 49 1, 50 2, 51 3, 52 4, 53 5, 54 6, 55 7, 56 8, 57 9,
