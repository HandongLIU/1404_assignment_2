"""(Incomplete) Tests for Book class."""
from book import Book


def run_tests():



    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.number_of_pages == 0
    assert not default_book.has_complete


    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, True)
    assert new_book.title == "Fish Fingers"
    assert new_book.author == "Dory"
    assert new_book.number_of_pages == 501
    assert new_book.has_complete


    new_book.mark_required()
    assert not new_book.is_completed
    assert new_book.is_required()

    assert new_book.is_long()

    another_book = Book("Book Title", "Author", 400)
    assert another_book.get_title() == "Book Title"
    assert another_book.get_author() == "Author"
    assert another_book.get_number_of_pages() == 400
    assert another_book.is_required()
    another_book.mark_complete()
    assert not another_book.is_required()
    assert not another_book.is_long()

run_tests()