from bookstore import Bookstore
from unittest import TestCase, main


class BookStoreTest(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(50)

    def test_the_constructor(self):
        self.assertEqual(50, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_books_limit_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Bookstore(0)

        expected = "Books limit of 0 is not valid"
        actual = str(ve.exception)
        self.assertEqual(expected, actual)

    def test_book_limit_valid_data(self):
        self.assertEqual(50, self.bookstore.books_limit)

    def test_the_len_method(self):
        test_bstore = Bookstore(20)
        test_bstore.availability_in_store_by_book_titles = {"Test1": 3, "Test2": 7}
        self.assertEqual(10, len(test_bstore))

    def test_receive_book_not_enough_space_raise_exception(self):
        book_store = Bookstore(1)
        with self.assertRaises(Exception) as ex:
            book_store.receive_book("Test1", 2)

        expected = "Books limit is reached. Cannot receive more books!"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_receive_book_if_enough_space_in_bookstore(self):
        book_store = Bookstore(20)
        book_store.availability_in_store_by_book_titles = {"Test1": 1}
        result = book_store.receive_book("Test2", 9)
        self.assertEqual("9 copies of Test2 are available in the bookstore.", result)
        self.assertEqual(2, len(book_store.availability_in_store_by_book_titles))

        result = book_store.receive_book("Test2", 1)
        self.assertEqual("10 copies of Test2 are available in the bookstore.", result)
        self.assertEqual(2, len(book_store.availability_in_store_by_book_titles))

    def test_sell_book_raise_exception_book_doesnt_exist(self):
        book_store = Bookstore(6)
        book_store.receive_book("Test1", 1)
        with self.assertRaises(Exception) as ex:
            book_store.sell_book("Test2", 1)

        expected = "Book Test2 doesn't exist!"
        actual = str(ex.exception)

        self.assertEqual(expected, actual)
        self.assertEqual({"Test1": 1}, book_store.availability_in_store_by_book_titles)

    def test_sell_book_not_enough_copies_raise_exception(self):
        book_store = Bookstore(6)
        book_store.receive_book("Test1", 2)
        with self.assertRaises(Exception) as ex:
            book_store.sell_book("Test1", 3)

        expected = "Test1 has not enough copies to sell. Left: 2"
        result = str(ex.exception)

        self.assertEqual({"Test1": 2}, book_store.availability_in_store_by_book_titles)
        self.assertEqual(expected, result)

    def test_sell_book_valid_data(self):
        book_store = Bookstore(10)
        sold_book = ("Maveric", 5)
        sold_book1 = ("Test", 1)
        book_store.receive_book(*sold_book)
        book_store.receive_book(*sold_book1)
        book_store.receive_book("Test2", 1)

        self.assertEqual("Sold 5 copies of Maveric", book_store.sell_book(*sold_book))
        self.assertEqual(5, book_store.total_sold_books)
        self.assertEqual("Sold 1 copies of Test", book_store.sell_book(*sold_book1))
        self.assertEqual(6, book_store.total_sold_books)


    def test_str_method(self):
        book_store = Bookstore(6)
        book_store.receive_book("Test1", 1)
        book_store.receive_book("Test2", 2)
        book_store.receive_book("Test3", 3)
        book_store.sell_book("Test3", 2)

        expected = f"Total sold books: 2\n" \
                   f'Current availability: 4\n' \
                   f' - Test1: 1 copies\n' \
                   f' - Test2: 2 copies\n' \
                   f' - Test3: 1 copies'

        self.assertEqual(expected, str(book_store))


if __name__ == "__main__":
    main()
