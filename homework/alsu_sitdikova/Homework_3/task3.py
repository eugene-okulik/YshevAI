"""Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
"""

n1, n2 = int(input()), int(input())

arithmetic_mean = (n1 + n2) / 2

geometric_mean = (n1 * n2) ** 0.5

print(arithmetic_mean)
print(geometric_mean)
