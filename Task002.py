# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
from math import ceil

def fill_list(n) -> list:
    u_list = []
    for i in range(n):
        u_list.append(randint(0, 10))
    return u_list

def multi_pairs(u_list) -> list:
    n_list = []
    for i in range(0, ceil(len(u_list) / 2)):
        n_list.append(u_list[i] * u_list[(i + 1) * (-1)])
    return n_list

try:
    n = int(input("Введите размер списка: "))
    source_list = fill_list(n)
    print(source_list)
    print(multi_pairs(source_list))
except:
    print("Нужно ввести число")