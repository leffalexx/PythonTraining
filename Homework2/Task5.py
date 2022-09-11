# 5. Реализуйте алгоритм перемешивания списка.

import random
from random import Random, randint



a = randint(5, 10)
my_list = []

for i in range (a):
    my_list.append(randint(0, 100))
print(my_list)

# random.shuffle(my_list)
# print(my_list)

for i in range (0, a - 1):
    new_index = random.randint(0, a -1)
    temp = my_list[i]
    my_list[i] = my_list[new_index]
    my_list[new_index] = temp
print(my_list)
