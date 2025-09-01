"""Дан такой словарь:
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
III
lovelovelovelove
итд
Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)
Помните, что копипаст одного и того же кода - плохо
"""

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def value_times_key(my_dict):
    for k, v in my_dict.items():
        print(k * v)


value_times_key(words)
