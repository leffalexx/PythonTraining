# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

my_list = []
for i in range(10):
    my_list.append(randint(-100, 100))
print(my_list)

def oddsum(given_list):
    sum = 0
    for i in range(1, len(given_list), 2):
        sum += given_list[i]
    return sum
print(oddsum(my_list))
