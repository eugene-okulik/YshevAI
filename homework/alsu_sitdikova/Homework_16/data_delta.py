"""В папке /homework/eugene_okulik/Lesson_16/hw_data лежит csv файл. Файл никуда не копируйте и не переносите.
Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные, которые там перечислены, в нашей базе данных.
"""


import dotenv
import os
import csv
import mysql.connector as mysql

from pathlib import Path


dotenv.load_dotenv()

parent_path = Path(__file__).parents[2]
file_pth = os.path.join(parent_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


def data_from_db():
    with mysql.connect(user=os.getenv('DB_USER'),
                       passwd=os.getenv('DB_PASSW'),
                       host=os.getenv('DB_HOST'),
                       port=os.getenv('DB_PORT'),
                       database=os.getenv('DB_NAME')) as db:
        cursor = db.cursor()
        select_query_join = """SELECT students.name, students.second_name, `groups`.title, books.title, subjects.title,
        lessons.title,  marks.value
        FROM students
        JOIN `groups` ON students.group_id = `groups`.id
        JOIN marks ON marks.student_id = students.id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjects ON lessons.subject_id = subjects.id
        JOIN books ON books.taken_by_student_id= students.id
        """

        cursor.execute(select_query_join)
        for i in cursor.fetchall():
            yield list(i)


db_output = data_from_db()


def data_from_csv(pth):
    with open(pth, newline='', encoding='UTF-8') as csv_file:
        file_data = csv.reader(csv_file)
        data = []
        for row in file_data:
            data.append(row)
        return data


csv_output = data_from_csv(file_pth)

for d in db_output:
    for c in csv_output:
        if d == c:
            print(f"Есть в базе: {d}")
            csv_output.remove(c)

print('Длина:', len(csv_output))
print('Оставшийся список:', *csv_output)
