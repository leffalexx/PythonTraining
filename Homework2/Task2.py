# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

number_1 = int(input('Введите число '))

my_list = []
temp = 1

for i in range(1, number_1 + 1):
    temp = temp * i
    my_list.append(temp)
print(my_list)