# 3. Задайте список из k чисел последовательности (1 + 1\k)^k
# и выведите на экран их сумму.

number_1 = int(input('Введите число k: '))
myarray = []

for i in range (1, number_1 + 1):
    myarray.append(round((1 + 1/i)**i, 2))
res = 0
for j in myarray:
    res = res + j
print(f'Сумма элементов последовательности равна {res}')