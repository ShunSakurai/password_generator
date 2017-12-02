# coding: utf-8
'''
cd Dropbox/Codes/password_generator
py password_generator.py
'''
import tkinter
import random
from re import search

view = tkinter.Frame()

subview_up = tkinter.Frame(view)
subview_left = tkinter.Frame(view)
subview_right = tkinter.Frame(view)
subview_up.grid(row=0, column=0, columnspan=2)
subview_left.grid(row=1, column=0, sticky='n')
subview_right.grid(row=1, column=1)

tuple_cc_sym = ((33, 48), (58, 65), (91, 97), (123, 127))
tuple_cc_alp = ((65, 91), (97, 123))
tuple_cc_num = ((48, 58),)


def mk_list_of_characters(tuple_cc):
    ls = []
    for tpl in tuple_cc:
        ls += [chr(c) for c in range(tpl[0], tpl[1])]
    return ls


ls_init_sym = mk_list_of_characters(tuple_cc_sym)
ls_init_alp = mk_list_of_characters(tuple_cc_alp)
ls_init_num = mk_list_of_characters(tuple_cc_num)

str_sym = ''.join(ls_init_sym)
str_alp = ''.join(ls_init_alp)
str_num = ''.join(ls_init_num)

var_str_sym = tkinter.StringVar(subview_up)
var_str_alp = tkinter.StringVar(subview_up)
var_str_num = tkinter.StringVar(subview_up)

var_str_sym.set(str_sym)
var_str_alp.set(str_alp)
var_str_num.set(str_num)

ent_sym = tkinter.Entry(subview_up, width=30, textvariable=var_str_sym)
ent_alp = tkinter.Entry(subview_up, width=30, textvariable=var_str_alp)
ent_num = tkinter.Entry(subview_up, width=30, textvariable=var_str_num)
entries = (ent_sym, ent_alp, ent_num)

for ent in entries:
    ent.pack()


var_bool_sym = tkinter.BooleanVar()
var_bool_alp = tkinter.BooleanVar()
var_bool_num = tkinter.BooleanVar()
variables_bool = (var_bool_sym, var_bool_alp, var_bool_num)

lname = ('sym', 'alp', 'num')
sw_sym = tkinter.Checkbutton(subview_left, text=lname[0])
sw_alp = tkinter.Checkbutton(subview_left, text=lname[1])
sw_num = tkinter.Checkbutton(subview_left, text=lname[2])
switches = (sw_sym, sw_alp, sw_num,)

for sw in switches:
    sw['variable'] = variables_bool[switches.index(sw)]
    sw.select()
    sw.pack()

var_length = tkinter.IntVar()
var_length.set(12)
var_choices = tkinter.IntVar()
var_choices.set(10)

l_length = tkinter.Label(subview_left, text='length')
l_length.pack()
sc_length = tkinter.Scale(subview_left, variable=var_length, from_=20, to=1, length=60, sliderlength=10, width=20)
sc_length.pack()
l_choices = tkinter.Label(subview_left, text='number')
l_choices.pack()
sc_choices = tkinter.Scale(subview_left, variable=var_choices, from_=20, to=1, length=60, sliderlength=10, width=20)
sc_choices.pack()


def get_available_char():
    ls_sym = list(var_str_sym.get())
    ls_alp = list(var_str_alp.get())
    ls_num = list(var_str_num.get())
    return {'sym': ls_sym, 'alp': ls_alp, 'num': ls_num}


def set_s():
    length = sc_length.get()
    dict_available_char = get_available_char()
    s = []
    if var_bool_sym.get() is True:
        s += dict_available_char['sym']

    if var_bool_alp.get() is True:
        s += dict_available_char['alp']

    if var_bool_num.get() is True:
        s += dict_available_char['num']

    if length > len(s):
        s = s * (length // len(s) + 1)

    return s


def set_pw(s):
    choices = sc_choices.get()
    length = sc_length.get()
    pw = ['']
    for k in range(choices):
        if var_bool_num.get() is True and length != 1:
            while search('[0-9]', pw[k]) is None:
                pw[k] = ''.join(random.sample(s, length))
            pw.append('')
        else:
            pw[k] = ''.join(random.sample(s, length))
            pw.append('')
    pw.remove('')
    return pw


def change_all_state(state):
    for child in subview_right.winfo_children():
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
    for child in subview_right.winfo_children():
        child.destroy()
    s = set_s()
    pw = set_pw(s)
    choices = sc_choices.get()
    buttons = [tkinter.Button(subview_right, text='') for k in range(choices)]
    for k in range(choices):
        buttons[k]['text'] = pw[k]
        buttons[k]['borderwidth'] = 1
        buttons[k].bind('<ButtonRelease-1>', button_tapped)
        buttons[k].grid(row=k)
    change_all_state('normal')


for sw in switches:
    sw['command'] = set_buttons

set_buttons()


def refresh_tapped(self):
    random.seed()
    set_buttons()


button_refresh = tkinter.Button(subview_left, text='refresh')
button_refresh['state'] = 'normal'
button_refresh.bind('<ButtonRelease-1>', refresh_tapped)
button_refresh.pack()

sc_length['command'] = refresh_tapped
sc_choices['command'] = refresh_tapped

top = view.winfo_toplevel()
top.resizable(False, False)
view.pack()
view.mainloop()
