# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# daynumber = int(input('Введите номер дня недели: '))
# if 1 <= daynumber <= 5:
#     print('Это будний день')
# elif daynumber == 6 or daynumber == 7:
#     print('Это выходной')
# else:
#     print('В неделе 7 дней, попробуйте еще раз')

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = input('Ведите число X: ')
# y = input('Ведите число Y: ')
# z = input('Ведите число Z: ')
# disjunction = not(x or y or z)
# conjunction = not x and not y and not z
# result = disjunction == conjunction
# print(result)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка.

# x = int(input('Ведите координату X: '))
# y = int(input('Ведите координату Y: '))
# if x > 0 and y > 0:
#     print('Точка находится на первой четверти плоскости')
# elif x > 0 and y < 0:
#     print('Точка находится на второй четверти плоскости')
# elif x < 0 and y < 0:
#     print('Точка находится на третьей четверти плоскости')
# elif x < 0 and y > 0:
#     print('Точка находится на четвертой четверти плоскости')
# else:
#     print('Точка расположена на одной из осей')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

# num1 = int(input('Укажите номер четверти: '))
# if num1 == 1:
#     print('x > 0 и y > 0')
# elif num1 == 2:
#     print('x > 0 и y < 0')
# elif num1 == 3:
#     print('x < 0 и y < 0')
# elif num1 == 4:
#     print('x < 0 и y > 0')
# else:
#     print('Четвертей всего четыре!')

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координату xA '))
y1 = int(input('Введите координату yA '))
x2 = int(input('Введите координату xB '))
y2 = int(input('Введите координату yB '))
result = ((x2 - x1)** 2 + (y2 -y1) ** 2) ** 0.5
result = round(result,2)
print("Расстояние между точками:", result) 
