import datetime
from loguru import logger
from bs4 import BeautifulSoup
from Wrapper.Types import Book, SearchResult
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.parse import quote
from bs4 import element


class Parser:
    """
    This class provides methods for parsing book information and performing book searches.
    """

    def __init__(self):
        """
        Constructor for the Parser class.
        """
        return None  # Constructor with no actual code

    def __by_id_inner(self, id: str, soup: BeautifulSoup) -> str | None:
        """
        Private method to extract content by element ID from a BeautifulSoup object.

        Args:
            id (str): The ID of the HTML element to find.
            soup (BeautifulSoup): The BeautifulSoup object to search in.

        Returns:
            str | None: The content of the element if found, or None if not found.
        """
        element = soup.find(id=id)
        if element:
            element = element.encode_contents().decode()
        return element

    def __by_id(self, id: str, soup: BeautifulSoup):
        """
        Private method to find an element by ID in a BeautifulSoup object.

        Args:
            id (str): The ID of the HTML element to find.
            soup (BeautifulSoup): The BeautifulSoup object to search in.

        Returns:
            element: The BeautifulSoup element if found, or None if not found.
        """
        element = soup.find(id=id)
        return element

    def parse_book_page(self, url) -> Book:
        """
        Parse a book page given its URL and return a Book object.

        Args:
            url (str): The URL of the book page to parse.

        Returns:
            Book: A Book object containing information about the parsed book.
        """
        BOOK = {}
        session = HTMLSession()
        r = session.get(url)
        print(r.status_code)

        # Retry the request up to 10 times if it doesn't return a 200 status code
        for i in range(10):
            if r.status_code != 200:
                r = session.get(url)
            else:
                break
        print(r.status_code)

        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find("h1", {"itemprop": "headline"})

        # Extract the book title if found
        if title:
            title = title.encode_contents().decode()

        ISBN = soup.find("span", {"itemprop": "isbn", "id": "book-publisher"})

        # Extract ISBN as an integer if found
        if ISBN:
            ISBN = int(ISBN.encode_contents().decode())

        BOOK["author"] = self.__by_id_inner(id="book-writer", soup=soup)
        BOOK["category"] = self.__by_id_inner(id="book-category", soup=soup)
        nop = soup.find("td", itemprop="numberOfPages")

        # Extract the number of pages as an integer if found
        if nop:
            nop = int(nop.encode_contents().decode().strip())

        BOOK["nop"] = nop
        BOOK["publisher"] = self.__by_id_inner(id="book-publisher", soup=soup)
        element = soup.find(
            "span",
            {
                "property": "dcterms:language",
                "itemprop": "inLanguage",
                "id": "book-category",
            },
        )

        # Extract the book's language if found
        if element:
            element = element.encode_contents().decode()

        BOOK["language"] = element
        link = soup.find(itemprop="image")

        # Extract the book's image URL if found
        if link:
            link = link["src"]

        # Construct the complete image URL or set it to None
        BOOK["img_url"] = "https://www.noor-book.com/" + str(link) if link else None

        # Create a Book object using the extracted information
        BOOK = Book(
            title=title,
            ISBN=ISBN,
            author=BOOK["author"],
            category=BOOK["category"],
            language=BOOK["language"],
            pages_count=BOOK["nop"],
            img_url=BOOK["img_url"],
        )

        return BOOK

    def search(self, query):
        """
        Search for books using a query and return a list of SearchResult objects.

        Args:
            query (str): The search query to find books.

        Returns:
            list[SearchResult]: A list of SearchResult objects containing book titles and URLs.
        """
        session = HTMLSession()
        query = quote(query)
        URL = "https://www.noor-book.com/?search_for=" + query.strip()
        r = session.get(URL)
        print(r.status_code)

        # Retry the request up to 10 times if it doesn't return a 200 status code
        for i in range(10):
            if r.status_code != 200:
                r = session.get(URL)
            else:
                break
        print(r.status_code)

        soup = BeautifulSoup(r.content, "html.parser")
        results = soup.find_all(
            "div", {"class": "book-restult", "itemtype": "http://schema.org/Book"}
        )
        BOOKS = []

        # Extract book titles and URLs from the search results
        for book in results:
            soup = BeautifulSoup(str(book), "html.parser")
            Element = soup.find("a", {"class": "img-a"})
            title = None
            url = None

            if Element:
                url = Element["href"]
                title = Element["title"]
                url = "https://www.noor-book.com" + quote(str(url))

            BOOKS.append(SearchResult(title=str(title), url=str(url)))

        return BOOKS
