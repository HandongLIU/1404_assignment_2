"""..."""


# Create your Book class in this file


class Book:
    def __init__(self, title, author, number_of_pages, has_complete=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.has_complete = has_complete

    def read(self):
        self.Read = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.Author

    def get_number_of_pages(self):
        return self.Number_of_Page

    def has_complete(self):
        return self.Read

    def __str__(self):
        return f"{self.title} by {self.author}, ({self.number_of_pages} pages)"
