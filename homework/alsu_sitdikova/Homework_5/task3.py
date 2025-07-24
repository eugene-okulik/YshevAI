"""Даны такие списки:
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
"""

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f"Students {students[0]}, {students[1]}, {students[2]} study these "
      f"subjects: {subjects[0]}, {subjects[1]}, {subjects[2]}")

print("Students {}, {}, {} study these subjects: {}, {}, {}".format(*students, *subjects))

print("Students %s, %s, %s study these subjects: %s, %s, %s" % (students[0], students[1], students[2],
                                                                subjects[0], subjects[1], subjects[2]))
