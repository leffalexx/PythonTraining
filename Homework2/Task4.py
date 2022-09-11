# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import Random, randint

n = int(input('Введите число N '))
myarray = []

for i in range (n):
    myarray.append(randint(-n, n))
print(myarray)

a, b = (int(i) for i in input('Введите через пробел позиции: ').split())

res = 1
for i in range (a - 1, b):
    res = res * myarray[i]
print(f'Произведение чисел между позициями {a} и {b} равно {res}')