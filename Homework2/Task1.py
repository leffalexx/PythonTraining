# 1. Напишите программу, которая принимает на вход вещественное число и показывает
#  сумму его цифр. Пример: - 0,56 -> 11

number_1 = input('Введите вещественное число ')
number_2 = number_1
number_1 = number_1.replace(',', '')
sum = 0
for i in number_1:
    sum = sum + int(i)
print(f'Сумма цифр в числе {number_2} равна {sum}')