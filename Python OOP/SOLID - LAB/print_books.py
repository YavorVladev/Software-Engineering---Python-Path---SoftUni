class Book:
    def __init__(self, title: str, author: str, content: str):
        self.content = content
        self.author = author
        self.title = title


class Formatter:
    def format(self, book: Book) -> str:
        return f"{book.title} is a book written by {book.author} and it's a {book.content}"


class MoviePosterPrinter:
    def format(self, book):
        return f"--------\n{book.title}\n-------\n{book.author}\n-------\n{book.content}\n-------\n"


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


normal_format = Formatter()
movie_formatter = MoviePosterPrinter()
b = Book("Harry Potter", "Yavor Vladev", "Book about some magical place")
normal_printer = Printer(normal_format)
movie_printer = Printer(movie_formatter)
print(normal_printer.get_book(b))
print()
print()
print(movie_printer.get_book(b))