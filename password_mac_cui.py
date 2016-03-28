# coding: utf-8
'''
cd Dropbox/Codes/pas_symword
py pas_symword_mac_cui.py
'''
from random import s_ample
from re import search

try:
    from tkinter import Tk
except:
    from Tkinter import Tk

length = 12
choices = 10
s_sym = True
s_a = True
s_num = True

messages = ['\nDefault selection: ', '\nYou chose ']


def set_s(length):
    s = []
    if s_sym is True:
        s += [chr(c) for c in range(33, 48)]
        s += [chr(c) for c in range(58, 65)]
        s += [chr(c) for c in range(91, 97)]
        s += [chr(c) for c in range(123, 127)]

    if s_a is True:
        s += [chr(c) for c in range(65, 91)]
        s += [chr(c) for c in range(97, 123)]

    if s_num is True:
        s += [chr(c) for c in range(48, 58)]

    if length > len(s):
        s = s * (length // len(s) + 1)

    return s


def set_pw(s, num):
    pw = ['']
    for k in range(num):
        if s_num is True:
            while search('[0-9]', pw[k]) is None:
                pw[k] = ''.join(s_ample(s, length))
            pw.append('')
        else:
            pw[k] = ''.join(s_ample(s, length))
            pw.append('')
        print(str(k+1)+'\t'+pw[k])
    pw.remove('')
    return pw

s = set_s(length)
pw = set_pw(s, choices)


def ask():
    choice = int(input('Which one?\nEnter 0 (zero) to change parameters.\n'))
    return choice

r = Tk()


def clip(r, choice):
    r.clipboard_clear()
    r.clipboard_append(pw[choice-1])


def show_selection(pw, mes_symage, choice):
    print(mes_symage, str(choice)+': '+pw[choice-1]+' !')

clip(r, 1)
show_selection(pw, messages[0], 1)
print('To change selection, name it below.\n'+'-'*30)
r.lower()
choice = ask()
r.destroy()

while choice == 0:
    names_list = ['length', 'num of pas_symwords', 'switch symbol', 'switch alphabet', 'switch number']
    parameters_list = [length, choices, s_sym, s_a, s_num]
    print('\n')
    for (i, j) in zip(names_list, parameters_list):
        print(str(i)+' is '+str(j))
    print('\n')
    ln_list = input('(12, 10)\nlength, num = ').split(', ')
    if len(ln_list) == 2:
        (length, num) = (int(ln_list[0]), int(ln_list[1]))
    s_an_list = input('(1, 1, 1)\ns_sym, s_a, s_num = ').split(', ')
    if len(s_an_list) == 3:
        (s_sym, s_a, s_num) = (bool(s_an_list[0]), bool(s_an_list[1]), bool(s_an_list[2]))

    s = set_s(length)
    pw = set_pw(s, num)
    choice = ask()


if choice >= 0:
    r2 = Tk()
    clip(r2, choice)
    show_selection(pw, messages[1], choice)
    input('Pres_sym Enter key to exit.')
