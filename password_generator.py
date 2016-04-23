# coding: utf-8
'''
cd Dropbox/Codes/password
py password_generator.py
'''
import tkinter
import random
from re import search

view = tkinter.Frame()

subview_left = tkinter.Frame(view)
subview_right = tkinter.Frame(view)
subview_left.grid(row=1, column=1)
subview_right.grid(row=1, column=0, sticky=tkinter.N)

var_sym = tkinter.IntVar()
var_alp = tkinter.IntVar()
var_num = tkinter.IntVar()
var = (var_sym, var_alp, var_num)

lname = ('sym', 'alp', 'num')
sw_sym = tkinter.Checkbutton(subview_right, text=lname[0])
sw_alp = tkinter.Checkbutton(subview_right, text=lname[1])
sw_num = tkinter.Checkbutton(subview_right, text=lname[2])
switch = (sw_sym, sw_alp, sw_num,)

for sw in switch:
    sw['variable'] = var[switch.index(sw)]
    sw.select()
    sw.pack()

var_length = tkinter.IntVar()
var_length.set(12)
var_choices = tkinter.IntVar()
var_choices.set(10)

l_length = tkinter.Label(subview_right, text='length')
l_length.pack()
sc_length = tkinter.Scale(subview_right, variable=var_length, from_=20, to=1, length=60, sliderlength=10, width=20)
sc_length.pack()
l_choices = tkinter.Label(subview_right, text='number')
l_choices.pack()
sc_choices = tkinter.Scale(subview_right, variable=var_choices, from_=20, to=1, length=60, sliderlength=10, width=20)
sc_choices.pack()


def set_s():
    length = sc_length.get()
    s = []
    if var_sym.get() == 1:
        s += [chr(c) for c in range(33, 48)]
        s += [chr(c) for c in range(58, 65)]
        s += [chr(c) for c in range(91, 97)]
        s += [chr(c) for c in range(123, 127)]

    if var_alp.get() == 1:
        s += [chr(c) for c in range(65, 91)]
        s += [chr(c) for c in range(97, 123)]

    if var_num.get() == 1:
        s += [chr(c) for c in range(48, 58)]

    if length > len(s):
        s = s * (length // len(s) + 1)

    return s


def set_pw(s):
    choices = sc_choices.get()
    length = sc_length.get()
    pw = ['']
    for k in range(choices):
        if var_num.get() == 1 and length != 1:
            while search('[0-9]', pw[k]) is None:
                pw[k] = ''.join(random.sample(s, length))
            pw.append('')
        else:
            pw[k] = ''.join(random.sample(s, length))
            pw.append('')
    pw.remove('')
    return pw


def change_all_state(state):
    for child in subview_left.winfo_children():
        child['state'] = state


def button_tapped(self):
    prefix = 'You chose '
    suffix = ' !'
    if self.widget['state'] == 'disabled':
        return
    elif self.widget['text'].startswith(prefix) is False:
        self.widget['text'] = prefix + self.widget['text'] + suffix
        self.widget['borderwidth'] = 2
        change_all_state('disabled')
        self.widget['state'] = 'normal'
    else:
        pass

    view.clipboard_clear()
    view.clipboard_append(self.widget['text'][len(prefix):-len(suffix)])


def set_buttons():
    for child in subview_left.winfo_children():
        child.destroy()
    s = set_s()
    pw = set_pw(s)
    choices = sc_choices.get()
    buttons = [tkinter.Button(subview_left, text='') for k in range(choices)]
    for k in range(choices):
        buttons[k]['text'] = pw[k]
        buttons[k]['borderwidth'] = 1
        buttons[k].bind('<ButtonRelease-1>', button_tapped)
        buttons[k].grid(row=k)
    change_all_state('normal')


for sw in switch:
    sw['command'] = set_buttons

set_buttons()


def refresh_tapped(self):
    random.seed()
    set_buttons()

button_refresh = tkinter.Button(subview_right, text='refresh')
button_refresh['state'] = 'normal'
button_refresh.bind('<ButtonRelease-1>', refresh_tapped)
button_refresh.pack()

sc_length['command'] = refresh_tapped
sc_choices['command'] = refresh_tapped

top = view.winfo_toplevel()
top.resizable(False, False)
view.pack()
view.mainloop()
