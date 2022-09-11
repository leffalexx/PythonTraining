# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import Random, randint

n = int(input('Введите число N '))
my_list = []

for i in range (n):
    my_list.append(randint(-n, n))
print(my_list)

a, b = (int(i) for i in input('Введите через пробел позиции: ').split())

res = my_list[a - 1] * my_list[b - 1]

print(f'Произведение чисел между позициями {a} и {b} равно {res}')