# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from inspect import trace
import random

def difference(u_list) -> float:
    max_value = min_value = u_list[0] % 1
    for i in range(1, len(u_list)):
        if u_list[i] % 1 > max_value:
            max_value = u_list[i] % 1
        if u_list[i] % 1 < min_value:
            min_value = u_list[i] % 1
    return round((max_value - min_value), 2)

def fill_list(n) -> list:
    u_list = []
    for i in range(n):
        u_list.append(round(random.randint(1, 10) + random.random(), 2))
    return u_list

try:
    n = int(input("Введите размер списка: "))
    source_list = fill_list(n)
    print(source_list)
    print(difference(source_list))
except:
    print("Нужно вводить чисело")
