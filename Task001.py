# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

def sum_odd_position(user_list) -> int:
    sum_odd = 0
    for i in range(1, len(user_list)):
        if i % 2 != 0:
            sum_odd += user_list[i]
    return sum_odd

def fill_list(n) -> list:
    u_list = []
    for i in range(n):
        u_list.append(randint(0, 10))
    return u_list

try:
    n = int(input("Введите разменость списка: "))
    source_list = fill_list(n)
    print(source_list)
    print(sum_odd_position(source_list))
except:
    print("Нужно ввести число")