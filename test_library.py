import pytest

@pytest.mark.P1
def test_list_books(library_with_books):
    assert "Amintiri din copilarie" in library_with_books.books
    assert "Moby Dick" in library_with_books.books
    assert "Lolita" in library_with_books.books
    assert "Bladerunner" in library_with_books.books

@pytest.mark.P1
def test_number_of_copies(library_with_books):
    assert library_with_books.books["Amintiri din copilarie"].copies == 5
    assert library_with_books.books["Moby Dick"].copies == 10
    assert library_with_books.books["Bladerunner"].copies == 7
    assert library_with_books.books["Lolita"].copies == 2

@pytest.mark.P1
def test_library_list_books(library_with_books):
    output = library_with_books.list_books()
    assert "Amintiri din copilarie | Ion Creanga | 5" in output
    assert "Moby Dick | Philip K. | 10" in output

@pytest.mark.P1
@pytest.mark.parametrize("title, expected, should_exist", [
    ("Not Existing Book", "Book Not Existing Book not found", False),
    ("Amintiri din copilarie", "Book Amintiri din copilarie removed", True),
    ("Moby Dick", "Book Moby Dick removed", True),])
def test_library_delete_book(library_with_books, title, expected, should_exist):
    result = library_with_books.remove_book(title)
    assert result == expected
    if should_exist:
        assert title not in library_with_books.books
    else:
        assert title not in library_with_books.books
        assert "Amintiri din copilarie" in library_with_books.books
        assert "Moby Dick" in library_with_books.books

@pytest.mark.P2
def test_user_no_books_borrowed(user_without_books):
    output = user_without_books.list_borrowed()
    assert output == "No books borrowed"


@pytest.mark.P1
def test_user_borrow_book(user_without_books, library_with_books):
    initial_book_copies = library_with_books.books["Amintiri din copilarie"].copies
    output = user_without_books.borrow_book(library_with_books, "Amintiri din copilarie")
    assert output == "Alex borrowed Amintiri din copilarie"
    assert user_without_books.borrowed_books["Amintiri din copilarie"] == 1
    assert library_with_books.books["Amintiri din copilarie"].copies == initial_book_copies - 1
