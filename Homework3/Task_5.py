# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(num):
    f_sequence = [0, 1]
    for i in range(num - 1):
        temp = f_sequence[len(f_sequence) - 1] + f_sequence[len(f_sequence) - 2]
        f_sequence.append(temp)
    j = 0
    for i in range(1, len(f_sequence)):
        negative = f_sequence[i + j] * ((-1) ** j)
        f_sequence.insert(0, negative)
        j += 1
    return(f_sequence)

k = int(input('Введите число: '))
print(fibonacci(k))