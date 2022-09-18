# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint
from typing import List


def unique(lis):
    mylist = []
    temp = 0
    for i in lis:
        temp = lis.count(i)
        if temp == 1:
            mylist.append(i)
    return mylist

list = [randint(1,11) for i in range(1, 11)]
print(list)
print(unique(list))
