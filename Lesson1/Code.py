# 1. Напишите программу, которая принимает на вход два числа и проверяет является ли одно число квадратом другого

# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# if (num_2 == (num_1 ** 2)) or (num_1 == (num_2 ** 2)):
#     print(True)
# else:
#     print(False)

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Линейно самостоятельно:

# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# num_3 = int(input('Введите число 3: '))
# num_4 = int(input('Введите число 4: '))
# num_5 = int(input('Введите число 5: '))

# max = num_1
# if num_2 > max:
#     max = num_2
# if num_3 > max:
#     max = num_3
# if num_4 > max:
#     max = num_4
# if num_5 > max:
#     max = num_5
# print(max)

# Списком и циклом:

# my_list = []
# for i in range(5):
#     num = int(input('--> '))
#     my_list.append(num)
#     maxx = my_list[0]
# for item in my_list[1:]:# срезаем первое число в списке, чтобы его с самим собой не сравнивать
#     if item > maxx:
#         maxx = item
# print(maxx)

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input('--> '))

# for i in range(-n, n + 1):
#     print(i, end = ' ') #end делвет вывод в строку


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number = input("Input number: ")

print(number[-2])


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30)


