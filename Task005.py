# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n(размерность вводим с клавиатуры), причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.
from random import randint

def create_array(row, col):
    array = [0] * row
    for i in range(row):
        array[i] = [0] * col
        for j in range(col):
            array[i][j] = randint(1, 9)
    return array

def print_array(array):
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            print(array[i][j], end=" ")
        print()

def shuffle_array(array, row, col):
    count_itr = 0
    stop_for = (row * col) / 2
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            r = randint(0, len(array) - 1)
            c = randint(0, len(array[i]) - 1)
            array[i][j], array[r][c] = array[r][c], array[i][j]
            count_itr += 1
            if count_itr >= stop_for:
                break
        if count_itr >= stop_for:
            break
    return array

row = int(input("Введите количество строк массива: "))
col = int(input("Введите количество столбцов массива: "))
array_user = create_array(row, col)
print_array(array_user)
print()
new_array = shuffle_array(array_user, row, col)
print_array(new_array)