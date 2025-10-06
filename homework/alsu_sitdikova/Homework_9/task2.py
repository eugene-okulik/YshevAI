"""map | filter
Есть такой список:
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.
Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
"""

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
                23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda x: x > 28, temperatures))

max_hot_day = max(hot_days)
min_hot_day = min(hot_days)
avg_hot_day = int(sum(hot_days) / len(hot_days))

print(hot_days)
print(max_hot_day)
print(min_hot_day)
print(avg_hot_day)
