# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from sympy import *

def summ(polynom_1, polynom_2, sum):
    x = Symbol('x')
    with open(polynom_1) as polynom_1, open(polynom_2) as polynom_2, open(sum, 'w') as sum :
        i, j = polynom_1.read(), polynom_2.read()
        i = i.replace('^', '**')   
        j = j.replace('^', '**')
        k = sympify(i + " + " + j)
        k = str(k)
        sum.write(k.replace('**', '^'))


summ('T5_1.txt','T5_2.txt','T5_merged.txt')


