from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import scrapy
from fake_useragent import UserAgent

import urllib.parse

from Wrapper.Types import Book


ua = UserAgent()


# EXECUTABLE_PATH = ("C:\\Users\\20106\\Documents\\Coding\\pythonprojects\\NoonWrapper\\Wrapper\\WebDriver\\chromedriver.exe")
class Scrpaer(scrapy.Spider):
    name = "my_spider"


def search(query: str) -> Book or [Book]:
    """
    :param query: STR a query to search on  https://www.noor-book.com/?search_for=[QUERY] ENDPOINT
    :return: Book or [Book]
    """
    endpoint: str = "https://www.noor-book.com/?search_for="
    url_encoded_query = urllib.parse.quote(query)
    resp = s.get(endpoint + url_encoded_query)
