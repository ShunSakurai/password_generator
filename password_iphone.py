# coding: utf-8

import ui
import clipboard
import random
from re import search

view = ui.View()
view.name = 'Password Generator'
view.background_color = 'white'
view.flex = ''

length = 12
choices = 10
s_sym = ui.Switch()
s_alp = ui.Switch()
s_num = ui.Switch()
switch = (s_sym, s_alp, s_num, )

for sw in switch:
    sw.value = True
    sw.center = (view.width * (switch.index(sw) + 0.55), view.height * 3.7)
    view.add_subview(sw)

l_sym = ui.Label()
l_alp = ui.Label()
ln = ui.Label()
Labels = (l_sym, l_alp, ln, )
lnames = ('sym', 'alp', 'num')
for l in range(len(Labels)):
    Labels[l].text = lnames[l]
    Labels[l].alignment = ui.ALIGN_CENTER
    Labels[l].center = (view.width * (l + 0.55), view.height * 4)
    view.add_subview(Labels[l])


def set_s():
    s = []
    if s_sym.value is True:
        s += [chr(c) for c in range(33, 48)]
        s += [chr(c) for c in range(58, 65)]
        s += [chr(c) for c in range(91, 97)]
        s += [chr(c) for c in range(123, 127)]

    if s_alp.value is True :
        s += [chr(c) for c in range(65, 91)]
        s += [chr(c) for c in range(97, 123)]

    if s_num.value is True:
        s += [chr(c) for c in range(48, 58)]

    if length > len(s):
        s = s * (length // len(s) + 1)

    return s


def set_pw(s):
    pw = ['']
    for k in range(choices):
        if s_num.value is True:
            while search('[0-9]', pw[k]) is None:
                pw[k] = ''.join(random.sample(s, length))
            pw.append('')
        else:
            pw[k] = ''.join(random.sample(s, length))
            pw.append('')
    pw.remove('')
    return pw


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
    s = set_s()
    pw = set_pw(s)
    for k in range(choices):
        buttons[k].title = pw[k]
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

button_refresh = ui.Button(title='refresh')


def set_refresh():
    button_refresh.center = (view.width * 0.5, view.height * 4.6)
    button_refresh.flex = 'W'
    button_refresh.font = ('<system-bold>', 16)
    button_refresh.enabled = True
    button_refresh.action = refresh_tapped
    view.add_subview(button_refresh)

for sw in switch:
    sw.action = refresh_tapped

set_refresh()
set_buttons()

view.present(orientations=['portrait'])
