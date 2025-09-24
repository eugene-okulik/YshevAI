"""
Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.
"""

import sys


def fibbonachi_nums():
    n = 0
    f_num = 1

    while True:
        yield n
        n, f_num = f_num, f_num + n


def get_num(n):
    count = 1
    for i in fibbonachi_nums():
        if count == n:
            print(i)
            break
        count += 1


get_num(5)
get_num(200)
get_num(10000)
get_num(100000)
