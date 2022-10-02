# 2. Найдите корни квадратного уровнения Ах^2 + Bx + C = 0,
# с помощью модуля. Запросите значения А,В,С 3 раза. Уравнения и корни запишите в файл.

from math import sqrt

print("Введите А, В, С")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2-4*a*c
with open('temp.txt', 'a', encoding='utf-8') as output:
    output.write(f"уравнение: {a}*x^2 + {b}*x + {c}\n")
    if d > 0 and a:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        output.write(f"корни уравнения: {x1} , {x2}\n")
    elif int(d) == 0:
        x = -b / (2*a)
        output.write("единственный корень: {x}\n")
    else:
        output.write("корней нет\n")

