# 3. Задайте два числа. Напишите прогр которая находит НОК(наим общее кратное) этих двух чисел
from math import gcd

def nok(num1, num2):
    return (num1*num2)//gcd(num1,num2)

a = int(input('первое число: '))
b = int(input('второе число: '))
print(nok(a,b))
