# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string_1 = 'Мы неабв очень любим Питон иабв Джавабв'

string_2 = 'абв'
my_list = string_1.split(' ')
res = [item for item in my_list if string_2 not in item]
print((" ".join(res)))