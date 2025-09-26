import pytest
from Library_project import Books, EBook, Library, User

def test_add_and_list_books():
    library = Library()
    book = Books("Amintiri din copilarie", "Ion Creanga", 5)
    library.add_book(book)

    assert "Amintiri din copilarie" in library.books
    assert library.books["Amintiri din copilarie"].copies == 5