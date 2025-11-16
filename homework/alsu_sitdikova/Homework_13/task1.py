"""Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
находит в нём даты и делает с этими датами то, что после них написано. Опирайтесь на то,
что структура каждой строки одинакова: сначала идет номер, потом дата, потом дефис и после него текст.
У вас должен получиться код, который находит даты и для даты под номером один в коде должно быть реализовано
то действие, которое написано в файле после этой даты. Ну и так далее для каждой даты.
"""
import datetime
import os.path


base_path = os.path.dirname(__file__)
hw_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), 'eugene_okulik', "hw_13", "data.txt")


def open_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            date_str = " ".join(line.split(" ")[1:3])
            yield datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")


date1 = next(open_file(hw_path)) + datetime.timedelta(days=7)
date2 = next(open_file(hw_path)).strftime("%A")
date3 = (datetime.datetime.now() - next(open_file(hw_path))).days


print(date1, date2, date3, sep="\n")
