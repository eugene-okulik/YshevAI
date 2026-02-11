import mysql.connector as mysql

with mysql.connect(user='st-onl',
                   passwd='AVNS_tegPDkI5BlB2lW5eASC',
                   host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
                   port='25060',
                   database='st-onl') as db:

    cursor = db.cursor(dictionary=True)

    insert_query_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
    insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    insert_query_groups = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
    update_query_students = "UPDATE students SET group_id=%s WHERE id=%s"
    insert_query_subjects = "INSERT INTO subjects (title) VALUES (%s)"
    insert_query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"

    cursor.execute(insert_query_student, ('Richelle_py', 'Test_py'))
    student_id = cursor.lastrowid
    print(student_id)

    cursor.executemany(insert_query_books, [
        ('Математический анализ, теория поля_py', student_id),
        ('Рассуждение о методе_py', student_id),
        ('Статистика для исследователей_py', student_id)])

    cursor.execute(insert_query_groups, ('qa_subjs_py', 'june 2025', 'april 2026'))
    group_id = cursor.lastrowid
    print(group_id)

    cursor.execute(update_query_students, (group_id, student_id))

    subjs = (f'math_{student_id}',
             f'philosophy_{student_id}',
             f'statistics_{student_id}')

    subjs_ids = []

    for s in subjs:
        cursor.execute(insert_query_subjects, (s,))
        subjs_ids.append(cursor.lastrowid)

    print(subjs_ids)

    lessons = [('math_analysis_py', subjs_ids[0]),
               ('lin_algebra_py', subjs_ids[0]),
               ('philosophy_ontology_py', subjs_ids[1]),
               ('philosophy_history_py', subjs_ids[1]),
               ('stat_math_py', subjs_ids[2]),
               ('stat_pract_py', subjs_ids[2])]

    lessons_ids = []

    for lesson in lessons:
        cursor.execute(insert_query_lessons, (*lesson,))
        lessons_ids.append(cursor.lastrowid)

    print(lessons_ids)

    cursor.executemany(insert_query_marks, [
        (5, lessons_ids[0], student_id),
        (5, lessons_ids[1], student_id),
        (4, lessons_ids[2], student_id),
        (4, lessons_ids[3], student_id),
        (5, lessons_ids[4], student_id),
        (5, lessons_ids[5], student_id),
    ])

    db.commit()

    #  Получите информацию из базы данных

    select_query_marks = "SELECT * FROM marks WHERE student_id=%s"
    select_query_books = "SELECT * FROM books WHERE taken_by_student_id=%s"
    select_query_join = """SELECT  students.name, students.second_name, `groups`.title,  `groups`.start_date,
    `groups`.end_date, marks.value, lessons.title, subjects.title, books.title
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjects ON lessons.subject_id = subjects.id
    JOIN books ON books.taken_by_student_id= students.id
    WHERE students.id = %s"""

    cursor.execute(select_query_marks, (student_id,))
    for i in cursor.fetchall():
        print(i)

    cursor.execute(select_query_books, (student_id,))
    for i in cursor.fetchall():
        print(i)

    cursor.execute(select_query_join, (student_id,))
    for i in cursor.fetchall():
        print(i)
