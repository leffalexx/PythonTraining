# В этом файле будет связь между блоками

import user_interface as uin

import logicc as l

def button():
    path = (r'C:\Документы\6. University\_GeekBrains\Python\PythonTraining\Homework7\data.csv')
    while True:
        try:
            user_action = int(uin.action())
        except:
            uin.err()
            continue
        if user_action == 1:
            l.find_contact(path)
            break
        elif user_action == 2:
            l.add_contact(path)
            break
        elif user_action == 3:
            l.remove_contact(path)
            break
        else: uin.err()