class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} with author {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            return f"Added new book with name ({book_name}) to the library"
        return f"Book ({book_name}) is already in the Library"

    def remove_book(self, book_name: str):
        if book_name not in self.books:
            return f"There is no such name as {book_name} in our library"
        return f"Removed {book_name} from our library"

    def find_book(self, book_name: str):
        try:
            return [book for book in self.books if book.title == book_name][0]
        except IndexError:
            "The book you're trying to find does not exist"



library = Library()
for book_number in range(1, 21):
    book = Book(f"Title {book_number}", f"Author {book_number}")
    library.add_book(book)

book1 = Book("Harry Potter", "Yavor")
print(book1)
print(library.add_book(book1))
print(library.add_book(book1))
print(library.find_book("Title 20"))
