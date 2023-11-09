import unittest
from Wrapper import Parser
from Wrapper.Types import *
class TestParser(unittest.TestCase):

    def test_parse_book_page(self):
        # Create a Parser instance
        parser = Parser()

        # Test data for a book page
        book_url = "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%85%D8%B9%D8%B1%D9%83%D8%A9-%D8%A7%D9%84%D8%A3%D8%AD%D8%B1%D8%A7%D8%B1-pdf"

        # Call the method and check if it returns a Book object
        book = parser.parse_book_page(book_url)
        self.assertIsInstance(book, Book)

    def test_search(self):
        # Create a Parser instance
        parser = Parser()

        # Test data for a search query
        query = "معركة الأحرار"

        # Call the method and check if it returns a list of SearchResult objects
        results = parser.search(query)
        self.assertIsInstance(results, list)
        for result in results:
            self.assertIsInstance(result, SearchResult)

class TestBookModel(unittest.TestCase):

    def test_create_book_instance(self):
        # Create a Book instance
        book = Book(
            title="معركة الأحرار",
            author="م احمد سمير",
            ISBN=None,
            pages_count=117
        )

        # Check if the instance was created successfully
        self.assertIsInstance(book, Book)

class TestSearchResultModel(unittest.TestCase):

    def test_create_search_result_instance(self):
        # Create a SearchResult instance
        result = SearchResult(
            title="معركة الأحرار",
            url="https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%85%D8%B9%D8%B1%D9%83%D8%A9-%D8%A7%D9%84%D8%A3%D8%AD%D8%B1%D8%A7%D8%B1-pdf"
        )

        # Check if the instance was created successfully
        self.assertIsInstance(result, SearchResult)

if __name__ == '__main__':
    unittest.main()

