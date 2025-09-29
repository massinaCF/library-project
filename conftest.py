import pytest
from library import Books, EBook, Library, User

@pytest.fixture
def library_with_books():
    lib= Library()
    book1= Books("Amintiri din copilarie", "Ion Creanga", 5)
    book2= Books("Moby Dick", "Philip K.", 10)
    book3 = EBook("Bladerunner", "Philip D. K", 7, 12)
    book4 = EBook("Lolita", "Nabukov", 2, 9)
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    lib.add_book(book4)

    yield lib

    lib.books.clear()