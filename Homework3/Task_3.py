# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.



my_list = [1.1, 1.2, 3.1, 10.01]

def difference(given_list):
    substracted_list = []
    for i in range(len(given_list)):
        j = given_list[i] % 1
        j = round(j, 2)
        substracted_list.append(j)
    res = max(substracted_list) - min(substracted_list)
    return res
print(difference(my_list))