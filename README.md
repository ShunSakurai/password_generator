# password
Simple password generators

[Japanese README](https://github.com/ShunSakurai/password/blob/master/README_jpn.md) is also available.

![UI](https://raw.github.com/wiki/ShunSakurai/password/password_ui.png)

## Description
The motivation behind this tool was to create a **simple** password generator that I can copy the password to clipboard with just one click.
Many programs and websites out there require three actions (drag on the password, right-click, and copy).

This tool is coded in Python with tkinter and is distributed in .exe format thanks to [py2exe](http://www.py2exe.org/), and in Mac .app format thanks to [py2app](https://pythonhosted.org/py2app/).

## Installation
It is currently available for Windows and Mac at [Releases](https://github.com/ShunSakurai/password/releases). iPhone version is also available as [Pythonista](http://omz-software.com/pythonista/) code. You can run it by using URL scheme pythonista://password_iphone.py or add it to Home screen using [Pythonista Shortcut](http://omz-software.com/pythonista/shortcut/).

### Windows
Installer is now being developed. For the moment, please do the following:

- Download dist.zip and decompress it
- Rename the folder to "Password" or any name you like
- Move it to C:\Program Files
- Create a shortcut of the .exe file and add it to your Desktop, to your tools folder, or to C:\ProgramData\Microsoft\Windows\Start Menu\Programs

This program needs to be **kept in the folder** to work. It does not work by itself.

### Mac
- Download Password.Generator.app.zip and decompress it
- Place the .app file somewhere you like. You can discard the folder
- Right-click Password Generator.app, click "Show Package Contents" and create an alias of Password Generator.app/Contents/MacOS/Password Generator
- Move the alias of Password Generator to "Applications" folder

## Usage
You can open the program by double-clicking Password Generator.exe / Password Generator or its alias.

In the right pane, click one of the choices. It is now copied to your clipboard!
Use the left pane to modify settings. You can switch symbols / alphabetical characters / numeral characters on and off. The length of a password and the number of choices can be set to any figure from 1 to 20.

![Selected](https://raw.github.com/wiki/ShunSakurai/password/password_selected.png)

The tool only generates passwords and allows you to copy one to the clipboard.
No storing feature is provided nor planned.

## Features to come
### Working on
- Making it [readable](http://www.amazon.com/dp/0596802293)
- Ability to store settings
- Preparing installer
- Preparing icon
- Elaborating design in the Windows version
- * Fix the bug where button is not re-enabled on Windows

### Maybe later
- Ability to edit characters used
- Keyboard shortcuts (e.g. 1 to 10)

Please let me know if you need any of the features as soon as possible.

## History

"*" at the beginning means bug-fixing.
For detailed history, please go to [Releases](https://github.com/ShunSakurai/password/releases).

### v1.1.0, March 31, 2016
- Distributed the binaries

### v1.0.0, March 28, 2016
- Added to GitHub
- Created Readme.md

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any feedback and contribution is welcome!

## License
You can use it for free.

© 2016 Shun Sakurai

## Basic idea
- Prepare a string containing the following characters
- Choose characters randomly from the string below
- If "num" checkbutton is on, and the "length" is 2 and over, the password contains at least one numeral character
- **No character is duplicated in one password**, unless the length of the string is shorter than the length of the password. This can be less secure, but I prefer the passwords look this way

> string = [chr(c) for c in range(33, 127)]
>
> Symbols
> 33 !, 34 ", 35 #, 36 $, 37 %, 38 &, 39 ', 40 (, 41 ), 42 *, 43 +, 44 ,, 45 -, 46 ., 47 /,
> 58 :, 59 ;, 60 <, 61 =, 62 >, 63 ?, 64 @,
> 123 {, 124 |, 125 }, 126~
>
> Alphabets
> 65 A, 66 B, 67 C, 68 D, 69 E, 70 F, 71 G, 72 H, 73 I, 74 J, 75 K, 76 L, 77 M, 78 N, 79 O, 80 P, 81 Q, 82 R, 83 S, 84 T, 85 U, 86 V, 87 W, 88 X, 89 Y, 90 Z,
> 91 [, 92 \, 93 ], 94 ^, 95 _, 96 `, 97 a, 98 b, 99 c, 100 d, 101 e, 102 f, 103 g, 104 h, 105 i, 106 j, 107 k, 108 l, 109 m, 110 n, 111 o, 112 p, 113 q, 114 r, 115 s, 116 t, 117 u, 118 v, 119 w, 120 x, 121 y, 122 z,
>
> Numbers
> 48 0, 49 1, 50 2, 51 3, 52 4, 53 5, 54 6, 55 7, 56 8, 57 9,

