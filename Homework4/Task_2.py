# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def multipliers(a):
    res = []
    i = 2
    while i**2 <= a:
        while a % i == 0:
            res.append(i)
            a = int(a / i)
        i += 1
    if a > 1:
        res.append(a)
    return res

n = int(input('Введите число N: '))
print(multipliers(n))


