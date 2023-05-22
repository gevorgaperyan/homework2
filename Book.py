import uuid


class Book:
    def __init__(self, name, author, year, isbn, genre, available_copies):
        self._name = name
        self._author = author
        self._isbn = isbn
        self._year = year
        self._genre = genre
        self._copies = []
        self._available_copies = available_copies

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre

    @property
    def copies(self):
        return self._copies

    @property
    def available_copies(self):
        return self._available_copies

    def add_copy(self, copy):
        self._copies.append(copy)
        self._available_copies.append(copy)

    def remove_copy(self, copy):
        if copy in self._copies:
            self.copies.remove(copy)
            self._available_copies.remove(copy)


class BookCopy:
    def __init__(self, book, copy_id):
        self._book = book
        self._copy_id = copy_id
        self._borrowed = False
        self._condition_rating = 0

    @property
    def book(self):
        return self.book

    @property
    def borrowed(self):
        return self._borrowed

    def borrowed_(self, value):
        self._borrowed = value
        if value:
            self.book.available_copies.remove(self)
        else:
            self.book.available_copies.append(self)

    @property
    def condition_rating(self):
        return self.condition_rating


def change_borrow_limit(student, limit):
    student.limit = limit


class Library:
    def __init__(self):
        self._books = []
        self._students = []

    def add_book(self, name, author, year, isbn, genre, available_copies):
        book = Book(name, author, year, isbn, genre, available_copies)
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def add_student(self, name, limit):
        student = Student(name, limit)
        self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    def get_all_books(self):
        return self._books

    def get_available_books(self):
        return [book for book in self._books]

    def search_books_by_name(self, name):
        return [book for book in self._books if name.lower() in book.name.lower()]

    def search_books_by_author(self, author):
        return [book for book in self._books if author.lower() in book.author.lower()]

    def search_books_by_genre(self, genre):
        return [book for book in self._books if genre.lower() in book.genre.lower()]


class Student:
    def __init__(self, name, limit=0):
        self.name = name
        self.borrowed_books = []
        self.limit = limit

    def __str__(self):
        return self.name

    def can_borrow(self):
        return len(self.borrowed_books) < self.limit

    def borrow_book(self, book):
        if self.can_borrow() and book:
            book.borrowed_by = self
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.borrowed_by = None
            self.borrowed_books.remove(book)

    def change_borrow_limit(self, limit):
        self.limit = limit

if __name__ == "__main__":
    book1 = Book("The Little Prince", ['Antoine de Saint-Exupéry'], 1943, "0-7567-5189-6", "fantasy novella",1)
    print(book1.available_copies)

