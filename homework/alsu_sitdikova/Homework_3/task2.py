"""Даны числа x и y. Получить x − y / 1 + xy
"""

x, y = int(input()), int(input())

print((x - y)/(1 + x*y))


# As a function aka definition
def get_expression(n1, n2):
    return (n1 - n2)/(1 + n1*n2)


print(get_expression(x, y))
