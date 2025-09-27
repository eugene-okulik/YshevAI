"""
Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool. Спросите у пользователя salary.
А bonus пусть назначается рандомом.
Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:
10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'
"""

import random

input_salary = int(input())
input_bonus = input()


def get_salary(salary, bonus):
    if bonus == "True":
        return f"{salary}, {bonus} - '${salary + int(random.random() * 100)}'"

    else:
        return f"{salary}, {bonus} - '${salary}'"


print(get_salary(input_salary, input_bonus))
