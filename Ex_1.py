# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число
# В качестве разделителя используйте пробел.
# in 11 23 90 -8 12 7 45
# out -44 90
# in 1. 6, 8: 9! -4
# out -4 9


def nums(string_val):
    for index in string_val:
        if not index.replace('-','').isdigit():
            return []
    return string_val

# num = input().split()
# print(nums(num))

def min_num(qwerty):
    art = nums(qwerty)
    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []
print(min_num(input().split()))