# 1. Вычислить число c заданной точностью d

import math

def rounding(a):
    a = len(a) - 2
    if a < 1:
        return 3
    else:
        return round(math.pi, a)

d = (input('Введите число d: '))
print(f'π с округлением до {d} равно {rounding(d)}')
    
