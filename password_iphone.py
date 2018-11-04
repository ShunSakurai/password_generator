# coding: utf-8

import ui
import clipboard
import random

view = ui.View()
view.name = 'Password Generator'
view.background_color = 'white'
view.flex = ''

l_sym = ui.Label()
l_cap = ui.Label()
l_low = ui.Label()
l_num = ui.Label()
labels = (l_sym, l_cap, l_low, l_num, )
lnames = ('sym', 'cap', 'low', 'num')

for l in range(len(labels)):
    labels[l].text = lnames[l]
    labels[l].alignment = ui.ALIGN_CENTER
    labels[l].center = (view.width * (l + 0.45) * 0.8, view.height * 3.6)
    view.add_subview(labels[l])

s_sym = ui.Switch()
s_cap = ui.Switch()
s_low = ui.Switch()
s_num = ui.Switch()
switches = (s_sym, s_cap, s_low, s_num, )

for sw in switches:
    sw.value = True
    sw.center = (view.width * (switches.index(sw) + 0.45) * 0.8, view.height * 3.9)
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

tuple_cc_sym = ((33, 48), (58, 65), (91, 97), (123, 127))
tuple_cc_cap = ((65, 91),)
tuple_cc_low = ((97, 123),)
tuple_cc_num = ((48, 58),)


def mk_list_of_characters(tuple_cc):
    ls = []
    for tpl in tuple_cc:
        ls += [chr(c) for c in range(tpl[0], tpl[1])]
    return ls


ls_sym = mk_list_of_characters(tuple_cc_sym)
ls_cap = mk_list_of_characters(tuple_cc_cap)
ls_low = mk_list_of_characters(tuple_cc_low)
ls_num = mk_list_of_characters(tuple_cc_num)


def get_available_char():
    list_string_list = []
    # Convert each list to another list
    # to prevent overwriting the original list in the later steps
    if s_sym.value:
        list_string_list.append(list(ls_sym))
    if s_cap.value:
        list_string_list.append(list(ls_cap))
    if s_low.value:
        list_string_list.append(list(ls_low))
    if s_num.value:
        list_string_list.append(list(ls_num))
    return list_string_list


def get_length():
    return int(sl_length.value * 10 + 5)


l_length.text = 'len: ' + str(get_length())


def set_pw():
    length = get_length()
    list_pw_string = []
    for k in range(choices):
        list_string_list = get_available_char()
        pw_list = []
        for string_list in list_string_list:
            random.shuffle(string_list)
            pw_list.append(string_list.pop())
        if len(pw_list) > length:
            list_pw_string.append(''.join(random.sample((list(pw_list)), length)))
            continue
        elif len(pw_list) == length:
            list_pw_string.append(''.join(pw_list))
        else:
            remaining_string = ''.join([''.join(ls) for ls in list_string_list])
            if length > len(pw_list) + len(remaining_string):
                remaining_string = remaining_string + ''.join([''.join(ls) for ls in get_available_char()]) * (length - len(pw_list) // len(remaining_string))
            pw_list.append(''.join(random.sample(remaining_string, length - len(pw_list))))
            random.shuffle(pw_list)
            list_pw_string.append(''.join(pw_list))
    return list_pw_string


def buttons_disable():
    for k in range(choices):
        buttons[k].enabled = False


def buttons_enable():
    for k in range(choices):
        buttons[k].enabled = True


def button_tapped(sender):
    prefix = 'You chose: '
    if not sender.title.startswith(prefix):
        clipboard.set(sender.title)
        sender.font = ('<system-bold>', 16)
        sender.title = prefix + sender.title
        buttons_disable()
        sender.enabled = True
    else:
        clipboard.set(sender.title[len(prefix):])


buttons = [ui.Button(title='') for k in range(choices)]


def set_buttons():
    list_pw_string = set_pw()
    for k in range(choices):
        buttons[k].title = list_pw_string[k]
        buttons[k].center = (view.width * 0.5, view.height * (3.1 * (k+0.5) / choices) + 30)
        buttons[k].flex = 'W'
        buttons[k].font = ('<sys-tem>', 16)
        buttons[k].action = button_tapped
        view.add_subview(buttons[k])
    buttons_enable()


def refresh_tapped(sender):
    list_pw_string = set_pw()
    for k in range(choices):
        buttons[k].title = list_pw_string[k]
        buttons[k].font = ('<sys-tem>', 16)
    buttons_enable()
    l_length.text = 'len: ' + str(get_length())


for sw in switches:
    sw.action = refresh_tapped

sl_length.action = refresh_tapped
button_refresh.action = refresh_tapped

set_buttons()

view.present(orientations=['portrait'])
