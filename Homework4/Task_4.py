# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

def polynomial(pwr):
    rndm = [randint(0, 100)]
    equasion = str(rndm[0])
    for i in range(1, pwr + 1):
        rndm.append(randint(0,100))
        equasion = f'{rndm[-1]}*x^{i} + '+ equasion
    equasion = equasion.replace('x^1 ','x ') 
    equasion = equasion.replace(' + 0','') 
    equasion = equasion.replace(' 1*',' ')
    equasion = equasion + ' = 0'
    return equasion

k = int(input("Введите натуральную степень k: "))

with open('Task_4.txt', 'w+') as file:
    file.write(polynomial(k))