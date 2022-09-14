# 3 Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).


def decimal_to_binary(num1):
    res = ''
    while num1 > 0:
        res = str(num1 % 2) + res
        num1 = num1//2
    return res

num = int(input('Введите число: '))
print(f'В двоичной системе {num} равно {decimal_to_binary(num)}')