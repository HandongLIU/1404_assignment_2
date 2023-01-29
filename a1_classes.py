"""..."""
# Copy your first assignment to this file, then update it to use Book class
# Optionally, you may also use BookCollection class

from book import Book

import csv

def main():
    print("Reading Tracker 1.0 - by Handong Liu")
    with open('books.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        book_list = []
        for row in csv_reader:
            book_list.append(row)

    class books:
        def __init__(self, Title="", Author=0, Pages=0.0):
            self.Title = Title
            self.Author = Author
            self.Pages = Pages
    MENU = "L - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        # List all books
        if choice == "L":
            with open("books.csv","r") as file:
                for line in file:
                    data = line.strip().split(',')
                    Title = data[0]
                    Author = data[1]
                    Pages = data[2]
                    book_list.append(books(Title, Author, Pages))
            for books in book_list:
                print(" {},  {}, {}".format(books.Title, books.Author, books.Page))
        #  Add new book
        elif choice == "A":
            Title = input("\nEnter book title: ")
            Author = input("Enter book author: ")
            Pages = input("Enter number of pages: ")
            # Error Checking
            if Pages.isdigit() and int(Pages) > 0:
                book_list.append(books(Title, Author, Pages))
                print("\nBook added.")
            else:
                print("\nInvalid page number.")

        # Mark a book as completed
        elif choice == "M":
            print("\nBook List: ")
            if len(book_list) == 0:
                print("No Books.")
            else:
                for i, book in enumerate(books):
                    print("{}. {} by {} ({} pages; {})".format(i + 1, book[0], book[1], book[2], book[3]))
                print("You need to read ", Total, " pages in ", i + 1, "books")

                book_num = input("\nSelect a book: ")
                # Error Checking
                if book_num.isdigit() and 0 < int(book_num) <= len(books):
                    if books[int(book_num) - 1][3] == "r":
                        print(book[1], "completed!")
                    else:
                        print("\nThat book is already completed")
                else:
                    print("\nInvalid selection.")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")
main()