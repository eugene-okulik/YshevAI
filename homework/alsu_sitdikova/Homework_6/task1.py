"""Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
dignissim vitae libero” и после этого выводит получившийся текст на экран. Знаки препинания не должны
оказаться внутри слова. Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
но уже преобразованного.
"""

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

for i in text.split(" "):
    if i.endswith(('.', ',')):
        print(f"{i[:-1]}ing{i[-1:]}", end=" ")
    else:
        print(f"{i}ing", end=" ")
