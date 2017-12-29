# coding: utf-8

import ui
import clipboard
import random
from re import search

view = ui.View()
view.name = 'Password Generator'
view.background_color = 'white'
view.flex = ''

l_sym = ui.Label()
l_alp = ui.Label()
l_num = ui.Label()
labels = (l_sym, l_alp, l_num, )
lnames = ('sym', 'alp', 'num')
for l in range(len(labels)):
    labels[l].text = lnames[l]
    labels[l].alignment = ui.ALIGN_CENTER
    labels[l].center = (view.width * (l + 0.55), view.height * 3.6)
    view.add_subview(labels[l])

s_sym = ui.Switch()
s_alp = ui.Switch()
s_num = ui.Switch()
switches = (s_sym, s_alp, s_num, )

for sw in switches:
    sw.value = True
    sw.center = (view.width * (switches.index(sw) + 0.55), view.height * 3.9)
    view.add_subview(sw)

choices = 10
sl_length = ui.Slider(value=0.71)
sl_length.center = (view.width * 1, view.height * 4.7)
sl_length.alignment = ui.ALIGN_CENTER
view.add_subview(sl_length)

l_length = ui.Label()
l_length.center = (view.width * 1, view.height * 4.4)
l_length.alignment = ui.ALIGN_CENTER
view.add_subview(l_length)

button_refresh = ui.Button(title='refresh')
button_refresh.center = (view.width * 1.2, view.height * 4.5)
button_refresh.alignment = ui.ALIGN_CENTER
button_refresh.flex = 'W'
button_refresh.font = ('<system-bold>', 16)
button_refresh.enabled = True
view.add_subview(button_refresh)


def get_length():
    return int(sl_length.value * 10 + 5)


l_length.text = 'len: ' + str(get_length())


def set_s():
    string_list = []
    length = get_length()

    if s_sym.value is True:
        string_list += [chr(c) for c in range(33, 48)]
        string_list += [chr(c) for c in range(58, 65)]
        string_list += [chr(c) for c in range(91, 97)]
        string_list += [chr(c) for c in range(123, 127)]

    if s_alp.value is True :
        string_list += [chr(c) for c in range(65, 91)]
        string_list += [chr(c) for c in range(97, 123)]

    if s_num.value is True:
        string_list += [chr(c) for c in range(48, 58)]

    if length > len(string_list):
        string_list = string_list * (length // len(string_list) + 1)

    return string_list


def set_pw(string_list):
    pw_list = []
    length = get_length()

    for k in range(choices):
        pw_list.append(''.join(random.sample(string_list, length)))
    return pw_list


def buttons_disable():
    for k in range(choices):
        buttons[k].enabled = False


def buttons_enable():
    for k in range(choices):
        buttons[k].enabled = True


def button_tapped(sender):
    prefix = 'You chose '
    suffix = ' !'
    if sender.title.startswith(prefix) is False:
        clipboard.set(sender.title)
        sender.font = ('<system-bold>', 16)
        sender.title = prefix + sender.title + suffix
        buttons_disable()
        sender.enabled = True
    else:
        clipboard.set(sender.title[len(prefix):-len(suffix)])


buttons = [ui.Button(title='') for k in range(choices)]


def set_buttons():
    string_list = set_s()
    pw_list = set_pw(string_list)
    for k in range(choices):
        buttons[k].title = pw_list[k]
        buttons[k].center = (view.width * 0.5, view.height * (3.1 * (k+0.5) / choices) + 30)
        buttons[k].flex = 'W'
        buttons[k].font = ('<sys-tem>', 16)
        buttons[k].action = button_tapped
        view.add_subview(buttons[k])
    buttons_enable()


def refresh_tapped(sender):
    s = set_s()
    pw = set_pw(s)
    for k in range(choices):
        buttons[k].title = pw[k]
        buttons[k].font = ('<sys-tem>', 16)
    buttons_enable()
    l_length.text = 'len: ' + str(get_length())


for sw in switches:
    sw.action = refresh_tapped

sl_length.action = refresh_tapped
button_refresh.action = refresh_tapped

set_buttons()

view.present(orientations=['portrait'])
