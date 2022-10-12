# Здесь будут описаны функции

import csv

import user_interface as uin

def find_contact(path):
    name = uin.input_name()
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ";" )
        for row in reader:
            if name == row[0]:
                print(*row)

def add_contact(path):
    name = uin.input_name()
    phone_number = uin.input_phone()
    new_contact = [name, phone_number]
    with open(path, 'a', newline = '') as data:
        writer = csv.writer(data, delimiter = ";")
        writer.writerow(new_contact)

def remove_contact(path):
    name = uin.input_name()
    lis = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ";")
        for row in reader:
            lis.append(row)
    for i in lis:
        if name in i:
            lis.remove(i)
            break
    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter = ";")
        writer.writerows(lis)


