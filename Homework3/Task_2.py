# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый 
# и последний элемент,второй и предпоследний и т.д.

from random import randint

my_list = []
for i in range(11):
    my_list.append(randint(-10, 10))
print(my_list)

def sum_of_couples(given_list):
    newarray = []
    for i in range(len(given_list) - (len(given_list) // 2)):
        mult = given_list[i] * given_list[len(given_list) - 1 - i]
        newarray.append(mult)
    return(newarray)

print(sum_of_couples(my_list))
