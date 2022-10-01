# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def descimal_to_binary(n) -> str:
    bin_n = f'{n % 2}'
    while n // 2 != 0:
        n //= 2
        bin_n = f'{n % 2}' + bin_n
    return bin_n

try:
    n = int(input("Введите натуральное число: "))
    b = descimal_to_binary(n)
    print(f"{n} -> {b}")
except:
    print("Нужно ввести число")
