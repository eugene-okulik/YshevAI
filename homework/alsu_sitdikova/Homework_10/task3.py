"""
Задание на декораторы 3
Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
(числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""


first_num, second_num = (int(i) for i in input().split())


def finish_me(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, operation='*')

        elif first == second:
            return func(first, second, '+')

        elif first > second:
            return func(first, second, '-')

        elif first < second:
            return func(first, second, '/')

    return wrapper


@finish_me
def calc(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            return first / second


print(calc(first_num, second_num))
