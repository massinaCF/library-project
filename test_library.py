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


def test_list_books(library_with_books):
    assert "Amintiri din copilarie" in library_with_books.books
    assert "Moby Dick" in library_with_books.books
    assert "Lolita" in library_with_books.books
    assert "Bladerunner" in library_with_books.books

def test_number_of_copies(library_with_books):
    assert library_with_books.books["Amintiri din copilarie"].copies == 5
    assert library_with_books.books["Moby Dick"].copies == 10
    assert library_with_books.books["Bladerunner"].copies == 7
    assert library_with_books.books["Lolita"].copies == 2

def test_library_list_books(library_with_books):
    output = library_with_books.list_books()
    assert "Amintiri din copilarie | Ion Creanga | 5" in output
    assert "Moby Dick | Philip K. | 10" in output


