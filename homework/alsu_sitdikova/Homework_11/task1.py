"""Создаём библиотеку
Первый класс
Создайте класс book с атрибутами:
материал страниц
наличие текста
название книги
автор
кол-во страниц
ISBN
флаг зарезервирована ли книга или нет (True/False).
Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
Создайте несколько (штук 5) экземпляров разных книг.
После создания пометьте одну книгу как зарезервированную.
Распечатайте детали о каждой книге в таком виде:
Если книга зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
если не зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
Второй класс
Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
предмет (типа математика, история, география),
класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
наличие заданий (bool)
Создайте несколько экземпляров учебников.
После создания пометьте один учебник как зарезервированный.
Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
если не зарезервирован:
Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9
"""


class Book:
    text_presence = True
    book_material = 'бумага'

    def __init__(self, book_name, author, page_count, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = ", зарезервирована" if is_reserved is True else ""

    def get_book_descr(self):
        print((f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, "
               f"материал: {self.book_material}{self.is_reserved}"))


class SchoolBook(Book):
    def __init__(self, material, book_name, author, page_count, is_reserved, subject, grade, is_exercise):
        super().__init__(material, book_name, author, page_count, is_reserved)
        self.subject = subject
        self.grade = grade
        self.is_exercise = is_exercise

    def get_book_descr(self):
        print((f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, "
               f"предмет: {self.subject}, класс: {self.grade}{self.is_reserved}"))


first_book = Book("Гордость и предубеждение", "Джей Остин", 350, 12345,  False)
second_book = Book("Мемуары Гейши", "Артур Голд", 240, 345, False)
third_book = Book("Идиот", "Достоевский", 500, 5467, False)
fourth_book = Book("Война и Мир", "Лев Толстой", 1005, 2342, True)
fifth_book = Book("Кайтусь-чародей", "Януш Корчак", 150, 234, False)


student_first_book = SchoolBook("Алгебра", "Иванов", 200, 34525,  False, "Математика", "7", True)
student_second_book = SchoolBook("Русский язык", "Петров", 300, 967, True, "Русский язык", 4, True)
student_third_book = SchoolBook("Окружающий мир", "Сидоров", 250, 761, False, "Биология", 5, False)


first_book.get_book_descr()
second_book.get_book_descr()
third_book.get_book_descr()
fourth_book.get_book_descr()
fifth_book.get_book_descr()

student_first_book.get_book_descr()
student_second_book.get_book_descr()
student_third_book.get_book_descr()
