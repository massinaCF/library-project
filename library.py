class Books(object):
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def get_info(self):
        return "%s | %s | %s" % (self.title, self.author, str(self.copies))

class EBook(Books):
    def __init__(self, title, author, copies, file_size):
        super().__init__(title, author, copies)
        self.file_size = file_size

    def get_info(self):
        return "%s | %s | %s | %sMB" % (self.title, self.author, str(self.copies), str(self.file_size))

class Library(object):

    def __init__(self):
        self.books = {}


    def get_title(self, book):
        string = book.get_info()
        string = string.split("|")
        title = string[0]
        return title

    def add_book(self, book):
        self.books[book.title] = book


    def list_books(self):
        if not self.books:
            return "No books available"
        book_infos = []
        for book in self.books.values():
            book_infos.append(book.get_info())
        result = "\n".join(book_infos)
        return result

    def remove_book(self, title):
        if title in self.books.keys():
            del self.books[title]
            return("Book %s removed" % title)
        else:
            return("Book %s not found" % title)

class User(object):
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, library, title):
        if title in library.books.keys() and library.books[title].copies > 0:
            library.books[title].copies -= 1

            if title in self.borrowed_books.keys():
                self.borrowed_books[title] += 1
            else:
                self.borrowed_books[title] = 1
            return self.name + " borrowed " + title
        else:
            return "Sorry %s not available." % title

    def return_book(self, library, title):
        if title in self.borrowed_books.keys():
            self.borrowed_books[title] -= 1
            library.books[title].copies += 1
            if self.borrowed_books[title] == 0:
                del self.borrowed_books[title]
            return self.name + " returned " + title
        else:
            return self.name + " doesn't have " + title

    def list_borrowed(self):
        if not self.borrowed_books:
            return "No books borrowed"
        else:
            for title, count in self.borrowed_books.items():
                return title + " borrowed in " + str(count) + " copies"





first_book = Books("Amintiri din copilarie", "Ion Creanga", 5)
second_book = EBook("Moby Dick", "Philip K.", 5, 10)
library = Library()
library.add_book(first_book)
library.add_book(second_book)
print(library.list_books())
library.remove_book("Ion Creanga")
print(library.list_books())

alex = User("Alex")
alex.borrow_book(library, "Amintiri din copilarie")
alex.borrow_book(library, "Moby Dick")
alex.borrow_book(library, "Amintiri din copilarie")
alex.list_borrowed()
alex.return_book(library, "Amintiri din copilarie")
alex.list_borrowed()



