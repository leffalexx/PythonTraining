# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint
from typing import List


def unique(lis):
    mylist = []
    for i in range (len(lis)):
            if lis[i] not in mylist:
                mylist.append(lis[i])
    return mylist
    
list = [randint(1,11) for i in range(1, 11)]
print(list)
print(unique(list))
