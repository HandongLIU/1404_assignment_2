"""(Incomplete) Tests for BookCollection class."""
from bookcollection import BookCollection
from book import Book


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection)
    assert not book_collection.books  # PEP 8 suggests not using len() to test for empty lists

    # Test loading books
    print("Test loading books:")
    book_collection.load_books('books.csv')
    print(book_collection)
    assert book_collection.books  # assuming CSV file is non-empty, length should be non-zero

    # Test adding a new Book with values
    print("Test adding new book:")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection)

    # Test sorting books
    print("Test sorting - author:")
    book_collection.sort("author")
    print(book_collection)
    # TODO: Add more sorting tests
    print("Test sorting - number of pages:")
    book_collection.sort("number_of_pages")
    print(book_collection)

    # TODO: Test get_required_pages()
    print("Test get_required_pages():")
    new_book_collection = BookCollection()
    assert new_book_collection.get_required_pages() == 0

    # TODO: Test saving books (check CSV file manually to see results)
    book_collection.save_books('books.csv')
    print(book_collection)

    # TODO: Add more tests, as appropriate
    another_book_collection = BookCollection()
    another_book_collection.add_book(Book("Book1", "Author1", 10, False))
    another_book_collection.add_book(Book("Book2", "Author2", 100, False))
    assert another_book_collection.get_required_pages() == 110
    assert another_book_collection.get_required_books() == 2
    assert len(another_book_collection.get_books()) == 2
    another_book_collection.sort("author")
    assert another_book_collection.get_books()[0].get_author() == "Author1"


run_tests()