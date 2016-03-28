# coding: utf-8
'''
cd Dropbox/Codes/password
py password_mac_cui.py
'''
from random import sample
from re import search

try:
    from tkinter import Tk
except:
    from Tkinter import Tk

length = 12
choices = 10
s_sym = True
s_alp = True
s_num = True

messages = ['\nDefault selection: ', '\nYou chose ']


def set_s(length):
    s = []
    if s_sym is True:
        s += [chr(c) for c in range(33, 48)]
        s += [chr(c) for c in range(58, 65)]
        s += [chr(c) for c in range(91, 97)]
        s += [chr(c) for c in range(123, 127)]

    if s_alp is True:
        s += [chr(c) for c in range(65, 91)]
        s += [chr(c) for c in range(97, 123)]

    if s_num is True:
        s += [chr(c) for c in range(48, 58)]

    if length > len(s):
        s = s * (length // len(s) + 1)

    return s


def set_pw(s, choices):
    pw = ['']
    for k in range(choices):
        if s_num is True:
            while search('[0-9]', pw[k]) is None:
                pw[k] = ''.join(sample(s, length))
            pw.append('')
        else:
            pw[k] = ''.join(sample(s, length))
            pw.append('')
        print(str(k+1)+'\t'+pw[k])
    pw.remove('')
    return pw

s = set_s(length)
pw = set_pw(s, choices)


def ask():
    choice = int(input('Which one?\nEnter 0 (zero) to change parameters.\n'))
    return int(choice)

r = Tk()


def clip(r, choice):
    r.clipboard_clear()
    r.clipboard_append(pw[choice-1])


def show_selection(pw, message, choice):
    print(message, str(choice)+': '+pw[choice-1]+' !')

clip(r, 1)
show_selection(pw, messages[0], 1)
print('To change selection, name it below.\n'+'-'*30)
r.lower()
choice = ask()
r.destroy()

while choice == 0:
    names_list = ['length', 'num of choices', 'switch symbol', 'switch alphabet', 'switch number']
    parameters_list = [length, choices, s_sym, s_alp, s_num]
    print('\n')
    for (i, j) in zip(names_list, parameters_list):
        print(str(i)+' is '+str(j))
    print('\n')
    ln_list = input('('+str(length)+', '+str(choices)+')\nlength, choices = ').split(',')
    if len(ln_list) == 2:
        (length, choices) = (int(ln_list[0]), int(ln_list[1]))
    san_list = input('('+str(int(s_sym))+', '+str(int(s_alp))+', '+str(int(s_num))+')\ns_sym, s_alp, s_num = ').split(',')
    if len(san_list) == 3:
        (s_sym, s_alp, s_num) = (bool(int(san_list[0])), bool(int(san_list[1])), bool(int(san_list[2])))

    s = set_s(length)
    pw = set_pw(s, choices)
    choice = ask()


if choice >= 0:
    r2 = Tk()
    clip(r2, choice)
    show_selection(pw, messages[1], choice)
    input('Press Enter key to exit.')
