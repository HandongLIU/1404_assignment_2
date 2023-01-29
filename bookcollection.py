"""..."""


# Create your BookCollection class in this file

from operator import attrgetter
from book import Book

class BookCollection:
    """..."""
    def __init__(self):
        self.books = []
    def load_books(self, filename):
        self.books.clear()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    title = parts[0]
                    author = parts[1]
                    number_of_pages = int(parts[2])
                    has_complete = parts[3] == "c"
                    book = Book(title, author, number_of_pages, has_complete)
                    self.add_book(book)
            return True
        except FileNotFoundError:
            return False
    def save_books(self, filename):
        """Save from book list into csv file"""
        with open(filename, "w", encoding="utf-8") as file:
            for book in self.books:
                row = [book.get_title(), book.get_author(), str(book.get_number_of_pages()),
                       "r" if book.is_required() else "c"]
                file.write(",".join(row) + "\n")

    def add_book(self, book):
        """Add a single Book object to the books."""
        if book is None:
            return
        self.books.append(book)

    def get_required_pages(self):
        """Get number of required pages."""
        required_pages = 0
        for book in self.books:
            if book.is_required():
                required_pages += book.get_number_of_pages()
        return required_pages

    def get_required_books(self):
        """Get number of required books."""
        required_books = 0
        for book in self.books:
            if book.is_required():
                required_books += 1
        return required_books

    def sort(self, attr=""):
        self.books.sort(key=attrgetter(attr, "title"))

    def get_books(self):
        return self.books

    def __str__(self):
        string = f"Page to read: {self.get_required_pages()}"
        for book in self.books:
            string += f"\n{book}"
        return string